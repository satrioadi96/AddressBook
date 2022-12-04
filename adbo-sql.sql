CREATE TABLE adbo (
	id serial PRIMARY KEY, 
	name CHARACTER VARYING(20) , 
	gender CHARACTER VARYING(10), 
	address CHARACTER VARYING(250), 
	phone_num CHARACTER VARYING(10), 
	age CHARACTER VARYING(3), 
	profession CHARACTER VARYING(30)
);


INSERT INTO adbo(id, name, gender, address, phone_num, age, profession)
VALUES (1, 'Adelia P.', 'Female', '', '078784738', '34', 'Docter') ;
INSERT INTO adbo(id, name, gender, address, phone_num, age, profession)
VALUES (2, 'Aditiya C.', 'Male', 'Pondok Sari', '067294667', '22', 'Student') ;
INSERT INTO adbo(id, name, gender, address, phone_num, age, profession)
VALUES (3, 'Arif H.', 'Male', '', '012968344', '13', 'Employee') ;
INSERT INTO adbo(id, name, gender, address, phone_num, age, profession)
VALUES (4, 'Cynthia A.', 'Female', 'Jl. Kemang 4', '', '9', 'Student') ;
INSERT INTO adbo(id, name, gender, address, phone_num, age, profession)
VALUES (5, 'Dana R.', 'Female', 'Perum Batu Indah', '088637112', '20', 'Freelancer') ;
INSERT INTO adbo(id, name, gender, address, phone_num, age, profession)
VALUES (6, 'Danang H.', 'Male', '', '073667321', '16', '') ;
INSERT INTO adbo(id, name, gender, address, phone_num, age, profession)
VALUES (7, 'Ernasanti', 'Female', 'Jl. Rasing 20', '', '', 'Analyst') ;
INSERT INTO adbo(id, name, gender, address, phone_num, age, profession)
VALUES (8, 'Erik R.', 'Male', 'Sukasari Mall', '033293859', '35', 'Director') ;
INSERT INTO adbo(id, name, gender, address, phone_num, age, profession)
VALUES (9, 'F. Ridwan', 'Male', 'Pantai Selatan 4', '088736211', '33', 'Employee') ;
INSERT INTO adbo(id, name, gender, address, phone_num, age, profession)
VALUES (10, 'Fadillatin S.', 'Female', '', '', '', '') ;
INSERT INTO adbo(id, name, gender, address, phone_num, age, profession)
VALUES (11, 'Ghani D.', '', 'Depok', '099372911', '20', 'Police') ;
INSERT INTO adbo(id, name, gender, address, phone_num, age, profession)
VALUES (12, 'Ghina B. C.', 'Female', 'Bojong aja', '093738271', '23', 'Nurse') ;


select * from adbo