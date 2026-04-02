--1-masala 
CREATE TABLE IF NOT EXISTS authors(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS books(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT NOT NULL,
	author_id INTEGER
);


INSERT INTO authors
(name)
VALUES
('Alisher Navoiy'),
('Abdulla Qodiriy'),
('Chingiz Aytmatov'),
('Otkir Hoshimov');



INSERT INTO books
(title, author_id)
VALUES
('Xamsa', 1),
('Otkan kunlar', 2),
('Asrga tutigulik kun', 3),
('Dunyoning ishlari', 4);
	


--2-masala
CREATE TABLE IF NOT EXISTS customers(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	phone INTEGER UNIQUE
);


CREATE TABLE IF NOT EXISTS orders(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	data REAL NOT NULL,
	customer_id INTEGER
);



INSERT INTO customers
(name, phone)
VALUES
('Ali', 9981234567),
('Laylo', 998909887768),
('Bekzod', 998936667777),
('Dilnoza', 998507743868);


INSERT INTO orders
(data, customer_id)
VALUES
('2025-08-01', 1),
('2025-08-03', 3),
('2025-08-05', 4),
('2025-08-08', 2);

