CREATE TABLE IF NOT EXISTS Book(
id integer primary key autoincrement,
title varchar,
pages int,
author varchar,
price float);

ALTER TABLE Book ADD COLUMN release_year int;

INSERT INTO Book(title, pages, author, price, release_year)
values('War and piece', 1000, 'M. Tank', 25, 1990),
('Romeo', 500, 'M. Tank', 20, 1999),
('Programming', 2000, 'M. Tank', 50, 2010),
('Python', 10000, 'M. Tank', 100, 2010),
('Lorem ipsum', 300, 'M. Tank', 5, 1900);

SELECT release_year, title, price FROM Book;

SELECT title, release_year, price FROM Book
WHERE release_year = 2010;

UPDATE Book SET price = 10
WHERE release_year = 2010;

DELETE FROM Book
WHERE price > 10;
