-- Asi se puede obtener la informacion de dos tablas relacionadas entre sí
select * from clientes inner join cuentas on clientes.id=cuentas.cliente_id;

-- Para declara un left JOIN que sería de manera obligatoria todo lo de la izquierda y opcionalmente lo de la derecha 
SELECT * FROM clientes LEFT JOIN cuentas ON clientes.id = cuentas.cliente_id;

SELECT * FROM cuentas LEFT JOIN clientes ON cuentas.cliente_id = clientes.id; 

-- Para declara un RIGHT JOIN que sería de manera obligatoria todo lo de la derecha y opcionalmente lo de la izquierda
SELECT * FROM clientes RIGHT JOIN cuentas ON clientes.id = cuentas.cliente_id; 

select clientes.id, nombre, cuentas.cliente_id,numero_cuenta from clientes 
left join cuentas on clientes.id=cuentas.cliente_id 

select cli.id id_cli, cli.nombre,cta.id id_cta, cta.numero_cuenta from clientes as cli
left join cuentas as cta on cli.id=cta.cliente_id;

select cli.id id_cli, cli.nombre,cta.id id_cta, cta.numero_cuenta from clientes cli
left join cuentas cta on cli.id=cta.cliente_id;


-- Ejercicio
-- Devolver la informacion (nombre, correo, status, numero_cuenta, tipo_moneda)
select cli.nombre, cli.email, cli.status, cta.numero_cuenta, cta.tipo_moneda
 from clientes cli
inner join cuentas cta on cli.id=cta.cliente_id;
-- Devolver la informacion de los usuario que tengan cuenta que no sea soles (solo el nombre y correo)
select cli.nombre, cli.email
  from clientes cli
left join cuentas cta on cli.id=cta.cliente_id
where cta.tipo_moneda!='SOLES';
-- Devolver el nombre, mantenimiento, tipo_moneda
select cli.nombre, cta.mantenimiento, cta.tipo_moneda
 from clientes cli
inner join cuentas cta on cli.id=cta.cliente_id;
-- Devolver el usuario (correo, nombre) y el tipo_moneda de los usuarios que tengan correo gmail y que su mantenimiento sea meno que 1.1 y que el usuario este activo
select cli.email, cli.nombre, cta.tipo_moneda
 from clientes cli
inner join cuentas cta on cli.id=cta.cliente_id
where cli.email ilike '%gmail.com' and cta.mantenimiento<1.1 and cli.activo;

-- Devolver cuantos clientes no tienen cuenta
select cli.* from clientes cli where not exists (select 1 from cuentas cta where cli.id=cta.cliente_id);

select count(cli.*) from clientes cli left join cuentas cta on cli.id=cta.cliente_id where numero_cuenta is null;

select cli.* from clientes cli left join cuentas cta on cli.id=cta.cliente_id where numero_cuenta is null;

create table movimientos (
 id serial PRIMARY KEY not null,
 cuenta_origen int null,
 cuenta_destino int not null,
 monto float not null,
 fecha_operacion timestamp default now(),
 CONSTRAINT movimientos_fk1 FOREIGN KEY(cuenta_origen) REFERENCES cuentas(id),
 CONSTRAINT movimientos_fk2 FOREIGN KEY(cuenta_destino) REFERENCES cuentas(id)
 );

ALTER TABLE movimientos alter COLUMN cuenta_destino DROP NOT null;

INSERT INTO movimientos (cuenta_origen, cuenta_destino, monto, fecha_operacion) VALUES
                        (null, 1, 100.10, '2024-07-01T14:15:17'),
                        (null, 2, 500.20, '2024-07-06T09:30:15'),
                        (null, 3, 650.00, '2024-07-06T15:29:18'),
                        (null, 4, 456.00, '2024-07-08T10:15:17'),
                        (null, 5, 500.00, '2024-07-10T17:18:24'),
                        (null, 6, 1050.24, '2024-07-04T12:12:12'),
                        (null, 7, 984.78, '2024-07-09TT11:06:49'),
                        (1,2, 40.30, '2024-07-10T10:10:10'),
                        (4,7, 350.00, '2024-07-16T20:15:35'),
                        (3, null, 50.00, '2024-07-16T22:15:10'),
                        (5, null, 100.00, '2024-07-17T10:19:25'),
                        (6, null, 350.28, '2024-07-18T14:15:16');

