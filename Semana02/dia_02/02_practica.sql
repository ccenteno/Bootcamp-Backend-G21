-- Crear una base datos llamada finanzas
CREATE DATABASE finanzas;

\connect finanzas

-- Crear una tabla en la cual registremos la informacion de los clientes de la siguiente manera:
-- id autoincrementable primary key
-- nombre texto no puede ser nulo
-- correo unico(no se repite) no puede ser nulo
-- status texto no puede ser nulo
-- activo booleano por defecto sea verdadero
-- fecha_creacion timestamp

create type status_enum as ENUM ('Buen Cliente','Cliente_Riesgoso','Cliente Peligroso');

CREATE TABLE CLIENTES (
id Serial not null primary key, 
nombre text not null,
email text not null unique, 
status text not null,
activo boolean default true, 
fecha_creacion timestamp default now());

insert into clientes values (default,'Cesar Centeno','ccentenor@gmail.com','Activo',true,CURRENT_TIMESTAMP);

drop table clientes;


alter table clientes alter column status TYPE status_enum

CREATE TABLE CLIENTES (
id Serial not null primary key, 
nombre text not null,
email text not null unique, 
status status_enum not null,
activo boolean default true, 
fecha_creacion timestamp default now());

insert into clientes values (default,'Cesar Centeno','ccentenor@gmail.com','Cliente_Riesgoso',true,CURRENT_TIMESTAMP);

-- para renombra una tabla
alter table finanzas RENAME to clientes;

alter table clientes alter column status TYPE status_enum using status::status_enum;

-- para ver la estructura de la tabla
\d clientes

INSERT INTO clientes (nombre, email, status, activo) VALUES
('Rodrigo Juarez Quispe', 'rjuarez@gmail.com', 'Buen Cliente', true),
('Mariana Sanchez Gil', 'msanchez@hotmail.com', 'Cliente_Riesgoso', true),
('Juliana Taco Martinez', 'jtaco@gmail.com', 'Buen Cliente', true),
('Gabriel Gonza Perez', 'ggonza@yahoo.es', 'Cliente Peligroso', false);

-- Mostrar todos los clientes que sea BUEN_CLIENTE
select * from clientes where status='Buen Cliente';
-- Mostrar todos los clientes que esten activos y que sean CLIENTE_RIESGOSO
select * from clientes where activo=true and status='Cliente_Riesgoso';
select * from clientes where activo and status='Cliente_Riesgoso';
-- Mostrar los clientes que tengan correo gmail o que sean CLIENTE_RIESGOSO
select * from clientes where email like '%gmail.com' or status='Cliente_Riesgoso';
-- Mostrar todos los clientes cuyo nombre tengan el apellido Gonza o Juarez y que no esten activos
select * from clientes where (nombre like '%Gonza%' or nombre like '%Juarez%') and activo=false;
select * from clientes where (nombre like '%Gonza%' or nombre like '%Juarez%') and not activo;
-- Mostrar todos los clientes cuyo nombre tengan el apellido Gonza o Juarez y que esten activos
select * from clientes where (nombre like '%Gonza%' or nombre like '%Juarez%') and activo=true;
select * from clientes where (nombre like '%Gonza%' or nombre like '%Juarez%') and activo;


-- Crear una tabla cuentas 
-- NOTA: NO CREAR LA TABLA

-- id autoincrementable primary key
-- numero_cuenta text not null unico,
-- tipo_moneda SOLES | DOLARES | EUROS no nulo
-- fecha_creacion timestamp valor actual del servidor no nulo
-- mantenimiento float puede ser nulo

create type tipo_moneda_enum as ENUM ('SOLES','DOLARES','EUROS');

-- Un cliente puede tener muchas cuentas PERO cada cuenta le va a pertenecer a un solo cliente
create table Cuentas (
 id Serial not null primary key,
 numero_cuenta text not null unique,
 tipo_moneda tipo_moneda_enum not null,
 fecha_creacion timestamp default now() not null,
 mantenimiento float null,
 -- RELACIONES
 cliente_id int not null,
 -- Llave foranea utilizando la columna cliente_id y va a hacer referencia a la columna id de la tabla clientes
 CONSTRAINT clientes_fk FOREIGN KEY(cliente_id) REFERENCES clientes(id)
);

INSERT INTO cuentas (numero_cuenta, tipo_moneda, fecha_creacion, mantenimiento, cliente_id) VALUES
('0f302b7e-41b6-45e9-950c-d2640f3ddcdf', 'SOLES', '2023-10-08T10:05', '1.5', '1'),
('7160f103-dc2a-4e67-9123-3d795bf4938b', 'SOLES', '2024-02-01T14:23', '1', '2'),
('b2eeb8ab-f06b-49df-8dac-332b2b48d7ff', 'DOLARES', '2020-12-08T16:17', '0', '1'),
('82c51e22-f4a6-4430-b401-05e458979c1b', 'SOLES', '2022-05-14T09:45', '1', '3'),
('57c54a3c-0a92-45b7-b888-0cbf827c93f8', 'SOLES', '2024-03-14T11:28', '1.2', '4'),
('c62ed24c-430b-462f-bdb3-ba79199bcffc', 'EUROS', '2023-10-04T12:27', '0.5', '3'),
('2343b92e-152a-4316-a4af-7406f8e551b8', 'SOLES', '2023-11-09T11:11', '0', '2');

select tipo_moneda, max(mantenimiento) from cuentas group by tipo_moneda;
select * from cuentas where (tipo_moneda, mantenimiento) in (select tipo_moneda, max(mantenimiento) from cuentas group by tipo_moneda);

select tipo_moneda, min(mantenimiento) from cuentas group by tipo_moneda;

-- Que cliente tiene mas cuentas


-- Mostrar los numeros de cuenta, su tipo de moneda y su fecha de creacion ordenada de la mas reciente a las mas antigua

-- Ingresar un nuevo cliente 
INSERT INTO clientes (nombre, email, status, activo) VALUES
('Eduardo de Rivero Manrique', 'ederivero@gmail.com', 'Buen Cliente', true);

select * from select max(cantidad) from (select cliente_id, count(cliente_id) cantidad from cuentas group by cliente_id) maximo;
