-- SQL script that creates a table users

CREATE TABLE IF NOT EXISTS users (
	id int PRIMARY KEY UNIQUE NOT NULL AUTO INCREMENT,
	email varchar(255) UNIQUE NOT NULL,
	name varchar(255)
);
