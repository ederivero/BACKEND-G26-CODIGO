SELECT * 
FROM profesores LEFT JOIN direcciones  -- LEFT JOIN devolvera todo lo de la izq y si tiene alguna relacion con la derecha
        ON profesores.id = direcciones.profesor_id;


-- Sirve para cambiar la visualizacion en formato de tabla a un formato de tarjetas
\x


-- Todos los profesores y si tienen direcciones tambien y sino, tambien
SELECT * 
FROM profesores AS prof LEFT JOIN direcciones AS dir
        ON prof.id = dir.profesor_id
ORDER BY prof.id ASC;


INSERT INTO direcciones (id, calle, numero, referencia, distrito, provincia, profesor_id) VALUES 
                        (DEFAULT, 'Los tulipanes', '120A', 'A dos cuadras de la cancha sintetica', 'Jesus Maria', 'Lima', null),
                        (DEFAULT, 'Los Jazmines', '1040A', null, 'Manuel Pastor', 'Moquegua', null),
                        (DEFAULT, 'Los Rosales', '2050A', 'Al frente del tambo', 'Cayma', 'Arequipa', null);


-- Todas las direcciones aun asi no tengan profesores asociados
SELECT * 
FROM profesores AS prof RIGHT JOIN direcciones AS dir
        ON prof.id = dir.profesor_id
ORDER BY dir.profesor_id DESC;


-- Esto devolvera todos los registros de los profesores aun asi no tengan direcciones asociadas y todas las direcciones aun asi no tengan profesores asociados
SELECT *
FROM profesores AS prof FULL OUTER JOIN direcciones AS dir
        ON prof.id = dir.profesor_id;




-- Mostrar los nombres de los profesores que vivan en Jesus Maria o Lima

-- Mostrar los correos de los profesores que vivan en el distrito de Trujillo y la provincia de  Cajabamba

-- Contar todos los profesores que tengan direcciones

-- Contar todos los profesores que tengan 2 o mas direcciones

-- Contar todos los profesores que no tengan direcciones asociadas
