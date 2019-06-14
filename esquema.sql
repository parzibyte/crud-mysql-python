/*
	Tutorial de CRUD con MySQL y Python 3
	parzibyte.me/blog
*/
CREATE DATABASE peliculas;
USE peliculas;
CREATE TABLE IF NOT EXISTS peliculas(
	id BIGINT UNSIGNED AUTO_INCREMENT NOT NULL,
	titulo VARCHAR(255) NOT NULL,
	anio SMALLINT NOT NULL,
	PRIMARY KEY(id)
);