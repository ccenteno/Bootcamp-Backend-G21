-- Así de define un comentario en las bases de datos
-- DDL (Data Definition Language) es un sublenguaje de SQL que sirve para definir como se almacenan los datos
CREATE DATABASE pruebas;

--  ABORT                            CREATE USER MAPPING
--  ALTER AGGREGATE                  CREATE VIEW
--  ALTER COLLATION                  DEALLOCATE
--  ALTER CONVERSION                 DECLARE
--  ALTER DATABASE                   DELETE
--  ALTER DEFAULT PRIVILEGES         DISCARD
--  ALTER DOMAIN                     DO
--  ALTER EVENT TRIGGER              DROP ACCESS METHOD
--  ALTER EXTENSION                  DROP AGGREGATE
--  ALTER FOREIGN DATA WRAPPER       DROP CAST
--  ALTER FOREIGN TABLE              DROP COLLATION
--  ALTER FUNCTION                   DROP CONVERSION
--  ALTER GROUP                      DROP DATABASE
--  ALTER INDEX                      DROP DOMAIN
--  ALTER LANGUAGE                   DROP EVENT TRIGGER
--  ALTER LARGE OBJECT               DROP EXTENSION
--  ALTER MATERIALIZED VIEW          DROP FOREIGN DATA WRAPPER
--  ALTER OPERATOR                   DROP FOREIGN TABLE
--  ALTER OPERATOR CLASS             DROP FUNCTION
--  ALTER OPERATOR FAMILY            DROP GROUP
--  ALTER POLICY                     DROP INDEX
--  ALTER PROCEDURE                  DROP LANGUAGE
--  ALTER PUBLICATION                DROP MATERIALIZED VIEW
--  ALTER ROLE                       DROP OPERATOR
--  ALTER ROUTINE                    DROP OPERATOR CLASS
--  ALTER RULE                       DROP OPERATOR FAMILY
--  ALTER SCHEMA                     DROP OWNED
--  ALTER SEQUENCE                   DROP POLICY
--  ALTER SERVER                     DROP PROCEDURE
--  ALTER STATISTICS                 DROP PUBLICATION
--  ALTER SUBSCRIPTION               DROP ROLE
--  ALTER SYSTEM                     DROP ROUTINE
--  ALTER TABLE                      DROP RULE
--  ALTER TABLESPACE                 DROP SCHEMA
--  ALTER TEXT SEARCH CONFIGURATION  DROP SEQUENCE
--  ALTER TEXT SEARCH DICTIONARY     DROP SERVER
--  ALTER TEXT SEARCH PARSER         DROP STATISTICS
--  ALTER TEXT SEARCH TEMPLATE       DROP SUBSCRIPTION
--  ALTER TRIGGER                    DROP TABLE
--  ALTER TYPE                       DROP TABLESPACE
--  ALTER USER                       DROP TEXT SEARCH CONFIGURATION
--  ALTER USER MAPPING               DROP TEXT SEARCH DICTIONARY
--  ALTER VIEW                       DROP TEXT SEARCH PARSER
--  ANALYZE                          DROP TEXT SEARCH TEMPLATE
--  BEGIN                            DROP TRANSFORM
--  CALL                             DROP TRIGGER
--  CHECKPOINT                       DROP TYPE
--  CLOSE                            DROP USER
--  CLUSTER                          DROP USER MAPPING
--  COMMENT                          DROP VIEW
--  COMMIT                           END
--  COMMIT PREPARED                  EXECUTE
--  COPY                             EXPLAIN
--  CREATE ACCESS METHOD             FETCH
--  CREATE AGGREGATE                 GRANT
--  CREATE CAST                      IMPORT FOREIGN SCHEMA
--  CREATE COLLATION                 INSERT
--  CREATE CONVERSION                LISTEN
--  CREATE DATABASE                  LOAD
--  CREATE DOMAIN                    LOCK
--  CREATE EVENT TRIGGER             MERGE
--  CREATE EXTENSION                 MOVE
--  CREATE FOREIGN DATA WRAPPER      NOTIFY
--  CREATE FOREIGN TABLE             PREPARE
--  CREATE FUNCTION                  PREPARE TRANSACTION
--  CREATE GROUP                     REASSIGN OWNED
--  CREATE INDEX                     REFRESH MATERIALIZED VIEW
--  CREATE LANGUAGE                  REINDEX
--  CREATE MATERIALIZED VIEW         RELEASE SAVEPOINT
--  CREATE OPERATOR                  RESET
--  CREATE OPERATOR CLASS            REVOKE
--  CREATE OPERATOR FAMILY           ROLLBACK
--  CREATE POLICY                    ROLLBACK PREPARED
--  CREATE PROCEDURE                 ROLLBACK TO SAVEPOINT
--  CREATE PUBLICATION               SAVEPOINT
--  CREATE ROLE                      SECURITY LABEL
--  CREATE RULE                      SELECT
--  CREATE SCHEMA                    SELECT INTO
--  CREATE SEQUENCE                  SET
--  CREATE SERVER                    SET CONSTRAINTS
--  CREATE STATISTICS                SET ROLE
--  CREATE SUBSCRIPTION              SET SESSION AUTHORIZATION
--  CREATE TABLE                     SET TRANSACTION
--  CREATE TABLE AS                  SHOW
--  CREATE TABLESPACE                START TRANSACTION
--  CREATE TEXT SEARCH CONFIGURATION TABLE
--  CREATE TEXT SEARCH DICTIONARY    TRUNCATE
--  CREATE TEXT SEARCH PARSER        UNLISTEN
--  CREATE TEXT SEARCH TEMPLATE      UPDATE
--  CREATE TRANSFORM                 VACUUM
--  CREATE TRIGGER                   VALUES
--  CREATE TYPE                      WITH
--  CREATE USER

-- \! cls  limpiar el contenido de la consola

-- \c o \connect pruebas

create table alumnos (
id Serial not null primary key, 
nombre text not null,
email text not null unique, 
matriculado boolean default true, 
fecha_nacimiento date null);
CREATE TABLE

alter table alumnos add column apellidos text;
ALTER TABLE
alter table alumnos add column email text not null unique;


 create table direcciones(id serial not null primary key, nombre text);

 drop table direcciones;

 drop database Nombre_bd;

 -- DML (Data manipulation languages)
 -- 
 \dT alumnos

 \d alumnos

 pruebas=# \dT alumnos
    Listado de tipos de dato
 Esquema | Nombre | Descripci¾n
---------+--------+-------------
(0 filas)


pruebas=# \d alumnos
                                   Tabla ½public.alumnos╗
     Columna      |  Tipo   | Ordenamiento | Nulable  |             Por omisi¾n
------------------+---------+--------------+----------+-------------------------------------
 id               | integer |              | not null | nextval('alumnos_id_seq'::regclass)
 nombre           | text    |              | not null |
 email            | text    |              | not null |
 matriculado      | boolean |              |          | true
 fecha_nacimiento | date    |              |          |
 apellidos        | text    |              |          |
═ndices:
    "alumnos_pkey" PRIMARY KEY, btree (id)
    "alumnos_email_key" UNIQUE CONSTRAINT, btree (email)


pruebas=# insert into alumnos (id, nombre, email, matriculado, fecha_nacimiento, apellidos)
pruebas-# values (default, 'Cesar', 'ccentenor@gmail.com', true, '1970-01-24', 'Centeno Rojas');
INSERT 0 1
pruebas=# select * from alumnos;
 id | nombre |        email        | matriculado | fecha_nacimiento |   apellidos
----+--------+---------------------+-------------+------------------+---------------
  1 | Cesar  | ccentenor@gmail.com | t           | 1970-01-24       | Centeno Rojas
(1 fila)

pruebas=# INSERT INTO alumnos VALUES (DEFAULT, 'Cesar', 'ccenteno@tecsup.edu.pe', DEFAULT, '1995-06-02', 'Centeno'), (DE
FAULT, 'Javier', 'jviiesse@gmail.com', FALSE, '2000-02-14', 'Wiesse'), (DEFAULT, 'Farit', 'fespinoza@gmail.com', TRUE, '
1990-07-28', 'Espinoza');
INSERT 0 3

pruebas=# select * from alumnos;
 id | nombre |         email          | matriculado | fecha_nacimiento |   apellidos
----+--------+------------------------+-------------+------------------+---------------
  1 | Cesar  | ccentenor@gmail.com    | t           | 1970-01-24       | Centeno Rojas
  2 | Cesar  | ccenteno@tecsup.edu.pe | t           | 1995-06-02       | Centeno
  3 | Javier | jviiesse@gmail.com     | f           | 2000-02-14       | Wiesse
  4 | Farit  | fespinoza@gmail.com    | t           | 1990-07-28       | Espinoza
(4 filas)

select * from alumnos where matriculado and id<3;
 id | nombre |         email          | matriculado | fecha_nacimiento |   apellidos
----+--------+------------------------+-------------+------------------+---------------
  1 | Cesar  | ccentenor@gmail.com    | t           | 1970-01-24       | Centeno Rojas
  2 | Cesar  | ccenteno@tecsup.edu.pe | t           | 1995-06-02       | Centeno
(2 filas)


select * from alumnos where matriculado or id<3;
 id | nombre |         email          | matriculado | fecha_nacimiento |   apellidos
----+--------+------------------------+-------------+------------------+---------------
  1 | Cesar  | ccentenor@gmail.com    | t           | 1970-01-24       | Centeno Rojas
  2 | Cesar  | ccenteno@tecsup.edu.pe | t           | 1995-06-02       | Centeno
  4 | Farit  | fespinoza@gmail.com    | t           | 1990-07-28       | Espinoza
(3 filas)
