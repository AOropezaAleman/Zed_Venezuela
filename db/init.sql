DROP DATABASE IF EXISTS saludos;

create database saludos;

\c saludos

CREATE TABLE saludo (
  id SERIAL PRIMARY KEY,
  created_at timestamp NOT NULL DEFAULT NOW(),
  mensaje VARCHAR(250) NOT NULL
);

create user admin with encrypted password 'admOro2024-';

GRANT ALL ON ALL TABLES IN SCHEMA public TO admin;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO admin;
GRANT ALL ON ALL FUNCTIONS IN SCHEMA public TO admin;
GRANT ALL ON SCHEMA public TO admin;
