FROM mdillon/postgis:10
COPY init.sql /docker-entrypoint-initdb.d/