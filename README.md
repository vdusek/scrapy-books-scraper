
<!-- --publish 5050:5050
```
docker run --detach --name pgadmin --network host thajeztah/pgadmin4
``` -->

The quickest way to start developing with Psycopg 3 is to install the binary packages by running:

This will install a self-contained package with all the libraries needed. You will need pip 20.3 at least: please run pip install --upgrade pip to update it beforehand.



Create a docker container postgres
```
docker run --detach --name postgres --publish 5432:5432 --env POSTGRES_PASSWORD=postgres --env POSTGRES_USER=postgres --env POSTGRES_DB=postgres postgres:16
```

Execute bash inside the postgres container in interactive mode
```
docker exec --interactive --tty postgres bash
```

Using psql command line tool connect to the databse `postgres`
```
psql --host localhost --port 5432 --username postgres --dbname postgres
```

List of tables
```
\dt
```

Create a table for books
```
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    rating INTEGER NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    in_stock BOOLEAN NOT NULL
);
```

Select all the rows in the table
```
SELECT * FROM books;
```
