# team-assignment3

- Perhatiin connect.py, jangan lupa diubah sesuai dengan konfigurasi mysql laptop masing masing
- Untuk databases bebas mau dinamain apa aja.
- Configurasi tables namanya users isinya jalanin syntax ini
``CREATE TABLE users (
id INT AUTO-INCREMENT PRIMARY KEY,
username VARCHAR(255),
email VARCHAR(255),
password VARCHAR(255),
name VARCHAR(255),
age INT,
gender VARCHAR(255),
job VARCHAR(255),
city VARCHAR(255),
rt INT,
rw INT, 
latitude FLOAT,
longitude FLOAT,
num VARCHAR(15)
)``
- Untuk menjalankan programnya, jalankan main.py

*Tambahan*
- Jalankan syntax  ``create table students (student_id int auto_increment primary key, name varchar(255), age int, class varchar(4), science_score int, math_score int, english_score int, bahasa_score int);``