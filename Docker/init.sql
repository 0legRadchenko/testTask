CREATE USER docker2 WITH SUPERUSER ENCRYPTED PASSWORD 'docker2';

CREATE DATABASE dockerdb2;
GRANT ALL PRIVILEGES ON DATABASE dockerdb2 TO docker2;