CREATE ROLE superset WITH LOGIN PASSWORD 'superset';
CREATE DATABASE superset_db OWNER superset;
CREATE USER examples WITH PASSWORD 'examples';
CREATE DATABASE examples_db OWNER examples;

