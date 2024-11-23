-- Usar la bd de prueba
\c prueba
\df

create table demostracion_triggers(
  id SERIAL PRIMARY KEY NOT NULL,
  mensaje TEXT,
  created_at timestamp default now()
  );

create function registrar_accion()
returns trigger as $$
BEGIN
   -- insertar un mensaje en la table de demostracion
   INSERT INTO demostracion_triggers(mensaje) values ('Se inserto un nuevo registro');
   -- NEW > será la informacion que me viene en el trigger, la informacion que se agregará ni bien se ejecute el trigger
   RETURN NEW;
END;
$$ LANGUAGE PLPGSQL;

CREATE TRIGGER trigger_registrar_registros
AFTER INSERT ON clientes
FOR EACH ROW --Cada vez que se haga un nuevo registro de un cliente se jecutará el trigger
EXECUTE FUNCTION registrar_accion();

INSERT INTO clientes (nombre, email, status, activo) VALUES
 ('Jose Martines Perez', 'jmartines@gmail.com', 'Buen Cliente', true);

select * from demostracion_triggers;

CREATE OR REPLACE FUNCTION crear_clientes_y_cuentas(
   nombre_cLiente TEXT, 
   correo_cliente TEXT, 
   status_cliente status_enum, 
   cliente_activo BOOLEAN, 
   tipo_moneda tipo_moneda_enum)
RETURNS VOID AS $$
-- Justo antes de empezar la función tenemos que declara las variables a utilizar en la función 
DECLARE
    nuevo_cliente_id INT; -- Este cliente_id lo usare para al momento de crear la cuenta relacionarlo con el
-- Inicia la ejecución de la función 
BEGIN
   -- RETURNING se puede llamar cuando hacemos un INSERT | UPDATE | DELETE y sirve para retorna la información resultante de la operación
   INSERT INTO clientes (nombre, email, status, activo) VALUES (nombre_cliente, correo_cliente, status_cliente,
    cliente_activo) RETURNING id INTO nuevo_cliente_id;
   -- Ahora procedemos a crear la cuenta del cliente
   INSERT INTO cuentas (numero_cuenta, tipo_moneda, cliente_id) VALUES ('', tipo_moneda, nuevo_cliente_id);
END;
$$ language plpgsql;

select crear_clientes_y_cuentas();

SELECT crear_clientes_y_cuentas('Shrek', 'shrek@dreamworks.com', 'Buen Cliente', TRUE, 'DOLARES'); 