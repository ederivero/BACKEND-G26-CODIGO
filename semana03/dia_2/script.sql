-- Crear una tabla llamada productos que tenga la siguiente info
-- id autoincrementable pk
-- nombre text no puede ser nulo
-- precio flotante no puede ser nulo
-- observacion text 
-- fecha_caducidad timestamp
-- fecha_creacion timestamp y cuyo valor por defecto sera now()
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio FLOAT NOT NULL,
    observacion TEXT,
    fecha_caducidad TIMESTAMP,
    fecha_creacion TIMESTAMP DEFAULT now()
);