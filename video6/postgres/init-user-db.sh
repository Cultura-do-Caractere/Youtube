#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "postgres" --dbname "postgres" <<-EOSQL
	CREATE USER app with password 'myapppassword';
	CREATE DATABASE app;
	GRANT ALL PRIVILEGES ON DATABASE app TO app;
EOSQL