CREATE TABLE IF NOT EXISTS Users(
id integer primary key autoincrement,
firstname varchar(255),
lastname varchar(255),
age integer);

INSERT INTO users(firstname, lastname, age)
values('Andrey', 'Ivanov', 35),
('Anton', 'Ivanov', 22),
('Evgeny', 'Bashura', 22),
('Danik', 'Andreev', 23),
('Olya', 'Arkadievna', 21);

SELECT firstname, lastname, age FROM users
WHERE firstname = 'Evgeny'

SELECT firstname, lastname, age FROM users
WHERE age < 25

SELECT firstname, lastname, age FROM users
WHERE age =< 18 AND age >= 15

UPDATE users SET age = 17
WHERE firstname = 'Olya';
