from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:1234@localhost:5432/addbook'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

CORS(app)

class Contact(db.Model):
    __tablename__ = 'adbo'
    id = db.Column(db.Integer, primary_key=True)
    name = db. Column(db.String(20))
    gender = db.Column(db.String(10))
    address = db.Column(db.String(250))
    phone_num = db.Column(db.String(10))
    age = db.Column(db.String(3))
    profession = db.Column(db.String(30))
    
    def __init__(self, name, gender, address, phone_num, age, profession):
        self.name = name
        self.gender = gender
        self.address = address
        self.phone_num = phone_num
        self.age = age
        self.profession = profession

    def __repr__(self):
        return "<Contact %r>" % self.name


@app.route('/')
def index():
    return jsonify({"message": "Welcome to ADDRES BOOK API! Enjoy your request here."})


@cross_origin()
@app.route('/adbo', methods=['POST', 'GET', 'DELETE'])
def data():

    # POST a data to database
    if request.method == 'POST':
        adbo_data = request.json
        
        name = adbo_data['name']
        gender = adbo_data['gender']
        address = adbo_data['address']
        phone_num = adbo_data['phone_num']
        age = adbo_data['age']
        profession = adbo_data['profession']

        data = Contact(
            name=name, gender=gender,
            address=address, phone_num=phone_num,
            age=age, profession=profession)
        db.session.add(data)
        db.session.commit()

        return jsonify({
            'response': 'Data (based on PostgreSQL) has been posted.',
            'success':True
        })

    # GET all data from database & sort by id
    if request.method == 'GET':
        all_adbo = []
        adbos = Contact.query.order_by(Contact.id).all()
        print(adbos)
        for adbo in adbos:
            results = {
                'id': adbo.id,
                'name': adbo.name,
                "gender": adbo.gender,
                "address": adbo.address,
                "phone_num": adbo.phone_num,
                "age": adbo.age,
                "profession": adbo.profession
            }
            all_adbo.append(results)
        return jsonify({
            "success": True,
            "all_contacts": all_adbo,
            "total_data": len(adbos),
        })
    
    # DELETE all data from database
    if request.method == 'DELETE':
        resData = Contact.query.all()
        db.session.delete(resData)
        db.session.commit()
        return jsonify({'status': 'All Data has been reset !'})
    


@cross_origin()
@app.route('/adbo/<string:id>', methods=['GET', 'DELETE', 'PUT'])
def onedata(id):

    # GET a specific data by id
    if request.method == 'GET':
        adbo = Contact.query.get(id)
        print(adbo)
        results = {
            'id': adbo.id,
            'name': adbo.name,
            "gender": adbo.gender,
            "address": adbo.address,
            "phone_num": adbo.phone_num,
            "age": adbo.age,
            "profession": adbo.profession
        }
        return jsonify(results)

    # DELETE a data
    if request.method == 'DELETE':
        delData = Contact.query.filter_by(id=id).first()
        db.session.delete(delData)
        db.session.commit()
        return jsonify({'status': 'ID Data '+id+' has been deleted !'})

    # UPDATE a data by id
    if request.method == 'PUT':
        adbo_data = request.json
        
        new_name = adbo_data['name']
        new_gender = adbo_data['gender']
        new_address = adbo_data['address']
        new_phone_num = adbo_data['phone_num']
        new_age = adbo_data['age']
        new_profession = adbo_data['profession']
        
        editData = Contact.query.filter_by(id=id).first()
        
        editData.name = new_name
        editData.gender = new_gender
        editData.address = new_address
        editData.phone_num = new_phone_num
        editData.age = new_age
        editData.profession = new_profession
        
        db.session.commit()
        return jsonify({'status': 'Data '+id+' is updated from PostgreSQL!'})

#------------------------------------------------------------------------

if __name__ == '__main__':
  app.run(debug=True)
