# Scrapy Books Scraper

- This project was created as part of the [Handling data in Scrapy: databases and pipelines](https://www.notion.so/apify/Handling-data-in-Scrapy-databases-and-pipelines-b57b3d7b0ee54c739b196300c116b595) blog post

<!-- Todo: pg admin -->
<!-- --publish 5050:5050 --->
<!-- docker run --detach --name pgadmin --network host thajeztah/pgadmin4 -->

```
poetry install
```

## Prepare database for storing data

Create a docker container postgres

```
docker run \
    --detach \
    --name postgres \
    --publish 5432:5432 \
    --env POSTGRES_USER=postgres \
    --env POSTGRES_PASSWORD=postgres \
    --env POSTGRES_DB=postgres \
    postgres:16
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

## Run the scraper

```
scrapy crawl book_spider
```
