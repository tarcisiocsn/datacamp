# Instroduction to SQL Server

> Lembrar que Query = Consulta


## Chapter 01 - SELECTion Box

### Select TOP()

```SQL
-- Return 5 rows

SELECT TOP(5) artist
FROM artists; 
```

<img width="410" alt="image" src="https://user-images.githubusercontent.com/68601128/120841841-62246d80-c542-11eb-9ffa-88596113ce1a.png">


```SQL
-- Return top 5% of rows

SELECT TOP(5) PERCENT artist
FROM artists; 
```

<img width="410" alt="image" src="https://user-images.githubusercontent.com/68601128/120842116-ad3e8080-c542-11eb-8498-08fd3dafd313.png">

### Select DISTINCT

```SQL
-- Return unique rows

SELECT DISTINCT nerc_region
FROM grid; 
```
<img width="407" alt="image" src="https://user-images.githubusercontent.com/68601128/120842356-f7276680-c542-11eb-80d1-197e67f19c6a.png">

### SELECT *

-- Return all rows

```sql
SELECT * 
FROM grid; 
```
+ * NOT * suitable for large tables

### ALIASING COLUMN NAMES WITH AS

```SQL
SELECT demand_loss AS lost_demand
FROM grid; 

-- or

SELECT description AS cause_of_outage
FROM grid;
```

### ORDERING AND FILTERING 

```sql
SELECT TOP10) prod_id, year_intro
FROM products
-- Order in ascending order
ORDER BY year_intro, product_id; 

/* Coloquei order by para os 2, pq possa ser que tenha 2 year_intro iguais e acabe não 
ficando na ordem por ano, então deixo os 2 se alinharem, lembrar que a ordem importa tbm*/

-- pode ser por DESC

SELECT TOP(10) prod_id, year_intro
FROM products
ORDER BY year_intro DESC, product_id;
```

<img width="351" alt="image" src="https://user-images.githubusercontent.com/68601128/120844356-a06f5c00-c545-11eb-9ae2-7e4053d8e987.png">


<img width="330" alt="image" src="https://user-images.githubusercontent.com/68601128/120844334-98afb780-c545-11eb-95bf-bd1eb1f69508.png">

> Podemos ordernar mesmo aqueles que não estão no SELECT statement

### WHERE -> Nesse capitulo não é muito diferente do que já aprendemos

+ Between

```sql
SELECT customer_id, total
FROM invoice 
WHERE total BETWEEN 20 AND 30; 
```
<img width="408" alt="image" src="https://user-images.githubusercontent.com/68601128/120844720-34412800-c546-11eb-9bdc-5bdc59f84773.png">

```SQL 
SELECT customer_id, total
FROM invoice
WHERE total NOT BETWEEN 20 AND 30;

``` 
<img width="366" alt="image" src="https://user-images.githubusercontent.com/68601128/120844841-5e92e580-c546-11eb-9f64-a203fb708abd.png">

### NULL

> Null indicates there is no value for that record 

```SQL
SELECT TOP(6) total, billing_state
FROM invoice
WHERE billing_state IS NULL; 
```
<img width="399" alt="image" src="https://user-images.githubusercontent.com/68601128/120845110-baf60500-c546-11eb-8e7e-6d92bb47079a.png">

```SQL
SELECT TOP(6) total, billing_state
FROM invoice
WHERE billing_state IS NOT NULL; 
```
<img width="406" alt="image" src="https://user-images.githubusercontent.com/68601128/120845157-ccd7a800-c546-11eb-88b0-8d26f29104d3.png">

**AND AGAIN**

```SQL
SELECT *
FROM songlist
WHERE
release_year = 1994
AND artist = 'Green Day'
AND song = 'Basket Case'; 
```
<img width="409" alt="image" src="https://user-images.githubusercontent.com/68601128/120850264-93566b00-c54d-11eb-8778-a606c09497a8.png">


```sql
SELECT *
FROM songlist
WHERE
release_year = 1994
AND artist = 'Green Day'
OR song = 'Basket Case'; 
```
<img width="400" alt="image" src="https://user-images.githubusercontent.com/68601128/120850312-a23d1d80-c54d-11eb-9e42-b96880ca48c4.png">

> Ai tá errado, como fixar isso?

+ By wrapping parentheses:

```sql
SELECT song 
FROM songlist
WHERE
artist = 'Green Day'
AND (
release_year = 1994
OR release_year = 2000
);

```
<img width="399" alt="image" src="https://user-images.githubusercontent.com/68601128/120850590-07910e80-c54e-11eb-8b09-33f603219e01.png">

> Another way for writing the query:

```sql
SELECT song 
FROM songlist
WHERE
(
artist = 'Green Day'3
AND release_year = 1994
)
OR (
artist = 'Green Day'
AND release_year > 2000
); 
```
**You can use 'IN'**

We can use IN  to perform a similar selection for either text or numeric values

```SQL
SELECT song, artist
FROM songlist
WHERE
artist IN ('Van Halen', 'ZZ Top')
ORDER BY song; 
```

<img width="413" alt="image" src="https://user-images.githubusercontent.com/68601128/120853119-8dfb1f80-c551-11eb-979b-d93e4d0ed770.png">

or

```SQL
SELECT song, release_year
FROM songlist
WHERE
release_year IN (1985, 1991, 1992)
```
> Se você prestar atenção, ele quer usar o where especificamente em alguma coluna, e ter o output com esses filtros. 

**You can use 'LIKE'**

You can use LIKE, along with  the percent sign (%)  to perfom wildcard  searches  on text fields.

```sql
SELECT song
FROM songlist
WHERE song LIKE 'a%';
```

<img width="404" alt="image" src="https://user-images.githubusercontent.com/68601128/120853726-7d977480-c552-11eb-90dd-3d82c5cb969b.png">

**EXAMPLE**

INSTRUCTIONS 1.1 

+ Retrieve the song, artist, and release_year columns from the songlist table.
+ Make sure there are no NULL values in the release_year column.
+ Order the results by artist and release_year.

```sql
-- Retrieve the song,artist and release_year columns
SELECT 
  song, 
  artist, 
  release_year 
FROM 
  songlist 
  -- Ensure there are no missing or unknown values in the release_year column
WHERE 
  release_year IS NOT NULL 
  -- Arrange the results by the artist and release_year columns
ORDER by 
  artist, release_year; 
```

**USING PARENTHESES IN YOUR QUERIES - EXAMPLE**

INSTRUCTIONS

+ Select all artists beginning with B who released tracks in 1986, but also retrieve any records where the release_year is greater than 1990.

```SQL
SELECT 
  artist, 
  release_year, 
  song 
FROM 
  songlist 
  -- Choose the correct artist and specify the release year
WHERE 
  (
    artist LIKE 'B%' 
    AND release_year = 1986
  ) 
  -- Or return all songs released after 1990
  OR release_year > 1990
  -- Order the results
ORDER BY 
  release_year, 
  artist, 
  song;
```

<img width="745" alt="image" src="https://user-images.githubusercontent.com/68601128/120855145-7d987400-c554-11eb-9cdf-33f413b2a2c2.png">








