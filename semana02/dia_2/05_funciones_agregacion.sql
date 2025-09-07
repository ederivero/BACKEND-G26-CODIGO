-- Retornara el numero total de registros
SELECT count(*) FROM profesores;

-- Si queremos agregar una columna "normal" tenemos que obligatoriamente usar el group by para que realice primero la agrupacion de estos elementos y luego proceda con el conteo de los mismos
SELECT count(*), activo FROM profesores GROUP BY activo;

SELECT * FROM profesores ORDER BY nombre ASC; -- ASC: A - Z | DESC: Z - A

-- Si tenemos dos ordenamientos el segundo entrara a funcionar si hay dos coincidencias con el primero 
SELECT * FROM profesores ORDER BY apellidos ASC, nombre ASC; -- ASC: A - Z | DESC: Z - A

-- Paginacion
-- OFFSET: indica cuantos registros me tengo que saltar 
SELECT * FROM profesores OFFSET 5;
-- LIMIT : indica cuantos registros quiero devolver
SELECT * FROM profesores LIMIT 5;

-- Agarrando los 5 primeros registros
SELECT * FROM profesores LIMIT 5 OFFSET 0;

-- Seleccionando los 5 segundos registros
SELECT * FROM profesores LIMIT 5 OFFSET 5;
SELECT * FROM profesores LIMIT 5 OFFSET 10;
SELECT * FROM profesores LIMIT 5 OFFSET 15;
SELECT * FROM profesores LIMIT 5 OFFSET 20;
SELECT * FROM profesores LIMIT 5 OFFSET 25;


-- Unico orden para utilizar SELECT con todas sus opciones
SELECT columna1, columna2, count(*)
FROM tabla
WHERE condicion1 AND condicion2 OR condicion3
GROUP BY columna1, columna2
ORDER BY columna1 ASC, columna2 DESC
LIMIt 1
OFFSET 0;


-- Mostrar todos los profesores que esten activos

-- Mostrar todos los profesores que tengan una fecha de contratacion del año pasado

-- Mostrar todos los profesores que se llamen Susan o se apelliden King

-- Mostrar todos los profesores cuyo correo sea hotmail.com o outlook.com o example.com

-- Mostrar el total de profesores que tengan correo gmail.com
