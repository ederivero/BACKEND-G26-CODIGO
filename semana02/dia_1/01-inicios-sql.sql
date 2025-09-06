-- Script : Archivo que se usa para ser ejecutado en la base de datos
-- SQL: Structured Query Language
-- DDL: Data Definition Language
-- CREATE: Crear entidades (BASE DE DATOS, TABLAS, USUARIOS, TRIGGER)
-- ALTER: Alterar (modificar) tablas, base de datos, usuarios, etc
-- DROP: Eliminar Entidades (tabla, base de datos, usuario)
-- TRUNCATE: Eliminar la data dentro de la tabla pero sin eliminar la tabla
-- RENAME: Cambiar el nombre de una entidad (BASE DE DATOS, TABLA, USUARIO, etc)
CREATE DATABASE pruebas;

-- NOTA: cuando usemos alguno de los comandos de PSQL no es necesario colocar ; al final
-- Lista las bases de datos que tenemos en el servidor
\l

-- Cambiamos a la base de datos que queremos utilizar
\c pruebas

-- \! sirve para poder ejecutar cualquier comando del sistema operativo dentro del psql
-- cls en windows es para limpiar la terminal
-- clear en mac es para limpiar la terminal
\! cls


CREATE TABLE personas (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT,
    correo TEXT UNIQUE, -- El correo jamas se va a repetir
    fecha_nacimiento TIMESTAMP -- Sirve para guardar el tiempo, adicional a ello se le puede indicar si queremos usar la zona horaria o no
);


-- DML: Data Manipulation Language
-- INSERT: ingresar nuevos datos a las tablas
-- SELECT: obtener la informacion de las tablas
-- UPDATE: actualizar la informacion de las tablas
-- DELETE: eliminar la informacion de las tablas

INSERT INTO personas VALUES (DEFAULT, 'Sebastian', null, 'sebas.aguero1107@gmail.com', '2003-11-07');

INSERT INTO personas (nombre, apellido, correo, fecha_nacimiento) VALUES
                     ('Eduardo', null, 'ederiveroman@gmail.com', '1992-08-01');

INSERT INTO personas VALUES (DEFAULT, 'Keing', 'Limache', 'klimache@gmail.com', '2005-02-05'),
                            (DEFAULT, 'Luis', 'Salas', 'lsalas@gmail.com', '2003-09-06'),
                            (DEFAULT, 'Jose', 'Ochoa', 'jochoa@outlook.com', '2000-06-06');

-- SELECT 
-- Seleccionar determinadas columnas
SELECT id, nombre FROM personas;

-- Seleccionar todas las columnas pertenecientes a la tabla
SELECT * FROM personas;

SELECT * FROM personas WHERE id > 3 AND apellido = 'Salas';

-- Mostrarme todas las personas que tengan el id entre 2 y 5 incluyendo el 5
SELECT * FROM personas WHERE id > 2 AND id <= 5;