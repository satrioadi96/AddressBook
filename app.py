from flask import Flask, render_template, request, redirect, url_for, flash, Response #, jsonify
import psycopg2  # pip install psycopg2
import psycopg2.extras
import io
import xlwt  # pip install xlwt


app = Flask(__name__)
app.secret_key = "satrio-postgre"

DB_HOST = "localhost"
DB_NAME = "address_book"
DB_USER = "postgres"
DB_PASS = "1234"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASS, host=DB_HOST)


# these are base functions fro every one route app

@app.route('/')
def Index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM contact"
    cur.execute(s)  # Execute the SQL
    list_users = cur.fetchall()
    return render_template('index.html', list_users=list_users)


@app.route('/add_contact', methods=['POST'])
def add_contact():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        address = request.form['address']
        phone_num = request.form['phone_num']
        age = request.form['age']
        profession = request.form['profession']

        cur.execute(
            "INSERT INTO contact (name, gender, address, phone_num, age, profession) VALUES (%s,%s,%s, %s, %s, %s)", (name, gender, address, phone_num, age, profession))
        conn.commit()
        flash('Contact Added Successfully')
        return redirect(url_for('Index'))


@app.route('/edit/<id>', methods=['POST', 'GET'])
def get_employee(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('SELECT * FROM contact WHERE id = {0}'.format(id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', contact=data[0])


@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        address = request.form['address']
        phone_num = request.form['phone_num']
        age = request.form['age']
        profession = request.form['profession']

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE contact
            SET name = %s,
                gender = %s,
                address = %s,
                phone_num = %s,
                age = %s,
                profession = %s
            WHERE id = %s
        """, (name, gender, address, phone_num, age, profession, id))
        flash('Contact Updated Successfully')
        conn.commit()
        return redirect(url_for('Index'))


@app.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete_contact(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('DELETE FROM contact WHERE id = {0}'.format(id))
    conn.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('Index'))

# deleting multiple data


@app.route('/delete', methods=['GET', 'POST'])
def index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
    #test = request.form.getlist('mycheckbox')
        for getid in request.form.getlist('mycheckbox'):
            print(getid)
            cur.execute('DELETE FROM contact WHERE id = {0}'.format(getid))
            conn.commit()
            flash('Contact Removed Successfully')
            return redirect('/')

# this route app only for excel file operation

@app.route('/download/report/excel')
def download_report():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM contact")
    result = cur.fetchall()
    # for row in result:
    # print(row)
    
    #output in bytes
    output = io.BytesIO()
    # create WorkBook object
    workbook = xlwt.Workbook()
    # add a sheet
    sh = workbook.add_sheet('Contact Report')
    
    # add headers
    sh.write(0, 0, 'ID')
    sh.write(0, 1, 'Name')
    sh.write(0, 2, 'Gender (Male/Female)')
    sh.write(0, 3, 'Address')
    sh.write(0, 4, 'Phone Number')
    sh.write(0, 5, 'Age')
    sh.write(0, 6, 'Profession')
    
    idx = 0
    for row in result:
        sh.write(idx+1, 0, str(row['id']))
        sh.write(idx+1, 1, row['name'])
        sh.write(idx+1, 2, row['gender'])
        sh.write(idx+1, 3, row['address'])
        sh.write(idx+1, 4, row['phone_num'])
        sh.write(idx+1, 5, row['age'])
        sh.write(idx+1, 6, row['profession'])
        idx += 1
        
    workbook.save(output)
    output.seek(0)
    return Response(output, mimetype="application/ms-excel", headers={"Content-Disposition": "attachment;filename=contact_report.xls"})

# route for insert data



if __name__ == "__main__":
    app.run(debug=True)
