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
> no caso o output só mostrará, em release_year, os anos de 1985, 1991 e 1992


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

### COUNT

The simplest COUNT query will return a count of the number of rows in that particular column.

> --


## CHAPTER 02

### SUMMING

Summing and counting are key ways of aggregating data, regardless (independentemente) of whether you are using a database, manipulating a spreadsheet, or using a programming language such as Python or R. Let's see how to do it in T-SQL using the grid table from Chapter 1.

You'll start by obtaining overall sums, focusing specifically on the 'MRO' region. 

<img width="476" alt="image" src="https://user-images.githubusercontent.com/68601128/120897457-a6744400-c5fc-11eb-9454-968453c1c203.png">

INSTRUCTIONS

+ Obtain a grand total of the `demand_loss_mw` column by using the `SUM` function, and alias the result as `MRO_demand_loss`.
+ Only retrieve rows `WHERE` `demand_loss_mw` is *not* `NULL` **and** `nerc_region` is `'MRO'`.


```sql
-- Sum the demand_loss_mw column
SELECT 
SUM(demand_loss_mw) AS MRO_demand_loss 
FROM 
  grid 
WHERE
  -- demand_loss_mw should not contain NULL values
  demand_loss_mw IS NOT NULL 
  -- and nerc_region should be 'MRO';
  AND nerc_region = 'MRO';
```
<img width="269" alt="image" src="https://user-images.githubusercontent.com/68601128/120897573-4205b480-c5fd-11eb-9365-3ec65b7b3047.png">


INSTRUCTIONS 1.2 - USING COUNT

+ Make the count more meaningful by restricting it to records where the nerc_region is 'RFC'. Name the result RFC_count.

> É pq na primeira instrução antes dessa, que não precisei tirar print, ele mandou fazer o COUNT de grid_id, no caso ele pegou o todo. Mas depois com o WHERE clause ai filtra melhor o RFC.
> 

```SQL
-- Obtain a count of 'grid_id'
SELECT 
  COUNT(grid_id) AS RFC_count
FROM 
  grid
-- Restrict to rows where the nerc_region is 'RFC'
WHERE
  nerc_region = 'RFC';
```
<img width="250" alt="image" src="https://user-images.githubusercontent.com/68601128/120897670-be989300-c5fd-11eb-9880-4c474e573a13.png">

### LEN

We can find the length of a text column (which means the number of characters, including spaces) using the LEN function. In this example, we first select the description column, and then the length of the description column, with a column alias. It's useful to know the total length of a string, as a starting point for use in other string calculations. 

<img width="621" alt="image" src="https://user-images.githubusercontent.com/68601128/120897803-51d1c880-c5fe-11eb-8789-cd6b14cd0caf.png">


### LEFT 

We can find the length of a text column (which means the number of characters, including spaces) using the LEN function. In this example, we first select the description column, and then the length of the description column, with a column alias. It's useful to know the total length of a string, as a starting point for use in other string calculations. 

<img width="567" alt="image" src="https://user-images.githubusercontent.com/68601128/120897949-200d3180-c5ff-11eb-8bdc-ee8a79d948d1.png">

### RIGHT

É a mesma coisa de left, maas de trás para frente

<img width="549" alt="image" src="https://user-images.githubusercontent.com/68601128/120897980-44690e00-c5ff-11eb-9f1b-9443065bce0e.png">

### CHARINDEX

The CHARINDEX function helps us find a specific character within a string. In this example, we're going to find the first underscore within the url column, from the courses table. The syntax is SELECT CHARINDEX,open parenthesis, then a single quote, then the character we want to find, in this case the underscore, a closing single quote, the name of the column we want to find the character within, then the closing parenthesis. Of course, we provide a column alias, and, for comparison purposes, we retrieve the url column so we can check that it works as expected. 

<img width="557" alt="image" src="https://user-images.githubusercontent.com/68601128/120898022-8a25d680-c5ff-11eb-9a7e-c1eab1234445.png">


### SUBSTRING

Sometimes we need to extract from the middle portion of a string, as opposed to from the left or right edges. That's a job for SUBSTRING. The syntax is SELECT SUBSTRING, open parenthesis, the column name, the number of the character to start from, then the number of characters to extract, then the closing parenthesis. Here we extract the string "datacamp.com", which,as we can see, begins a few characters in from the left hand edge. 

<img width="544" alt="image" src="https://user-images.githubusercontent.com/68601128/120898114-e25cd880-c5ff-11eb-9715-b7204d4f55a9.png">


### REPLACE

Finding and replacing text is a common task, so let's see how we can do this in T-SQL. We've seen how to find, using CHARINDEX, but, we don't need to use it for this task. Instead, the REPLACE function does the hard work for us. In this example, we replace all underscores in the url column with hyphens. We don't need to specify the positions of the character, or even that there are more than one - REPLACE does the job for us and all instances of an underscore are replaced.

<img width="506" alt="image" src="https://user-images.githubusercontent.com/68601128/120898204-3ff12500-c600-11eb-890b-8fe62f9c5b42.png">


**Stuck in the middle with you**

INSTRUCTIONS 1.1

+ You can use CHARINDEX to find a specific character or pattern within a column. Edit the query to return the CHARINDEX of the string 'Weather' whenever it appears within the description column.

```sql
-- Complete the query to find `Weather` within the description column
SELECT 
  description, 
  CHARINDEX('Weather', description) 
FROM 
  grid
WHERE description LIKE '%Weather%';
```

<img width="942" alt="image" src="https://user-images.githubusercontent.com/68601128/120905703-51e7bd80-c62a-11eb-9095-6109abb78de1.png">

INSTRUCTIONS 1.2

+ We now know where 'Weather' begins in the description column. But where does it end? We could manually count the number of characters, but, for longer strings, this is more work, especially when we can also find the length with LEN.

```SQL
-- Complete the query to find the length of `Weather'
SELECT 
  description, 
  CHARINDEX('Weather', description) AS start_of_string,
  LEN('Weather') AS length_of_string 
FROM 
  grid
WHERE description LIKE '%Weather%'; 
```

<img width="898" alt="image" src="https://user-images.githubusercontent.com/68601128/120905724-6e83f580-c62a-11eb-9eb0-de810b80a611.png">


INSTRUCTIONS 1.3

+ Now we use SUBSTRING to return everything after Weather for the first ten rows. The start index here is 15, because the CHARINDEX for each row is 8, and the LEN of Weather is 7.

```SQL
-- Complete the substring function to begin extracting from the correct character in the description column
SELECT TOP (10)
  description, 
  CHARINDEX('Weather', description) AS start_of_string, 
  LEN ('Weather') AS length_of_string, 
  SUBSTRING(
    description, 
    15, 
    LEN(description)
  ) AS additional_description 
FROM 
  grid
WHERE description LIKE '%Weather%';
```

<img width="679" alt="image" src="https://user-images.githubusercontent.com/68601128/120906087-f79c2c00-c62c-11eb-8c08-8765c0161b3e.png">


### Grouping Error

It wouldn't make sense to try and aggregate the description field as it is not a numeric column. However, by using the GROUP BY clause, which splits the data up into groups according to the values within the chosen column, and then applies the aggregation function, the query now works. We return a total sum for each description, including rows where the demand_loss value is NULL. 

<img width="866" alt="image" src="https://user-images.githubusercontent.com/68601128/120906219-f0295280-c62d-11eb-82c6-495502aa2bcb.png">

tem que ter cuidado com esse tipo de erro, por isso precisar usar o group by

<img width="847" alt="image" src="https://user-images.githubusercontent.com/68601128/120906238-164ef280-c62e-11eb-8e95-12501920c97c.png">

### HAVING

Let's recap what we've learned so far. We know we can use aggregate functions in our SELECT statement, and that we should provide a meaningful column alias. We apply filters to the data using WHERE. And we now know we can split the data into groups using GROUP BY. When we write a WHERE clause, the filtering takes place on the row level - that is, within the data. But, for example, what if we want to sum values based on groups, and then filter on those sums? 

As a reminder, here is our existing query and result set. If we wanted to filter the lost_demand column of our results, how would we do it? We've already applied a WHERE clause. We could try adding an additional WHERE clause, but that would only affect the underlying row values, and NOT our overall grouped lost_demand values. How can we filter the results of this query to restrict the results to those where the sum of demand_loss_mw was greater than 1000? 

<img width="846" alt="image" src="https://user-images.githubusercontent.com/68601128/120906362-359a4f80-c62f-11eb-9245-0b8cdffe5eba.png">

The answer is by adding a HAVING clause, after the GROUP BY clause. By typing HAVING, then SUM, then our desired column name in brackets, and then the condition we want to apply, we arrive at the final result set we need. 

<img width="847" alt="image" src="https://user-images.githubusercontent.com/68601128/120906369-45199880-c62f-11eb-8d0d-b7f63b76dbd5.png">

**SUMMARY**

Here's a quick overview of what we've covered. The main things to remember are that GROUP BY splits your results up into combinations of 1 or more columns - so for example if you wanted to break sales by territory, you would group by territory. Our chosen aggregation functions are then applied to those groups HAVING clauses are applied after the GROUP BY, and are used to either filter on the groups, or to filter using aggregate values such as SUM or AVG (average). 

**EXAMPLES**

In an earlier exercise, you wrote a separate WHERE query to determine the amount of demand lost for a specific region. We wouldn't want to have to write individual queries for every region. Fortunately,you don't have to write individual queries for every region. With GROUP BY, you can obtain a sum of all the unique values for your chosen column, all at once. ( Essa questão é falando sobre aquele mapa dos eua e os desastres)

You'll return to the grid table here and calculate the total lost demand for all regions.

INSTRUCTIONS 

+ Select nerc_region and the sum of demand_loss_mw for each region.
+ Exclude values where demand_loss_mw is NULL.
+ Group the results by nerc_region.
+ Arrange in descending order of demand_loss.

```SQL
-- Select the region column
SELECT 
  nerc_region,
  -- Sum the demand_loss_mw column
  SUM(demand_loss_mw) AS demand_loss
FROM 
  grid
  -- Exclude NULL values of demand_loss
WHERE 
  demand_loss_mw IS NOT NULL
  -- Group the results by nerc_region
GROUP BY
  nerc_region
  -- Order the results in descending order of demand_loss
ORDER BY 
  demand_loss DESC;
```

<img width="752" alt="image" src="https://user-images.githubusercontent.com/68601128/120906480-1d770000-c630-11eb-9a70-d6b62c7b9301.png">

**EXAMPLE 2**

HAVING - 

WHERE is used to filter rows before any grouping occurs. Once you have performed a grouping operation, you may want to further restrict the number of rows returned. This is a job for HAVING. In this exercise, you will modify an existing query to use HAVING, so that only those results with a sum of over 10000 are returned.

INSTRUCTIONS

+ Modify the provided query to remove the WHERE clause.
+ Replace it with a HAVING clause so that only results with a total demand_loss_mw of greater than 10000 are returned.

```SQL
SELECT 
  nerc_region, 
  SUM (demand_loss_mw) AS demand_loss 
FROM 
  grid 
  -- Remove the WHERE clause
WHERE demand_loss_mw  IS NOT NULL
GROUP BY 
  nerc_region 
  -- Enter a new HAVING clause so that the sum of demand_loss_mw is greater than 10000
HAVING
  SUM(demand_loss_mw) > 10000
ORDER BY 
  demand_loss DESC;
```  
<img width="743" alt="image" src="https://user-images.githubusercontent.com/68601128/120906536-9bd3a200-c630-11eb-9ed9-90bead70b605.png">

## CHAPTER 03

### INNER JOINS - A PERFECT MATCH

INSTRUCTIONS FOR THE EXAMPLE

+ Perform an inner join between album and track using the album_id column.

`Track` table

<img width="1218" alt="image" src="https://user-images.githubusercontent.com/68601128/120907390-44850000-c637-11eb-9e08-e551b51f5914.png">

`album` table

<img width="1216" alt="image" src="https://user-images.githubusercontent.com/68601128/120907396-4f3f9500-c637-11eb-968d-ef7b78df46ed.png">

`artist` table

```SQL
SELECT 
  track_id,
  name AS track_name,
  title AS album_title
FROM track
  -- Complete the join type and the common joining column
INNER JOIN album 
ON track.album_id = album.album_id;
```

OUTPUT 

<img width="1209" alt="image" src="https://user-images.githubusercontent.com/68601128/120907398-59619380-c637-11eb-914d-2b5aa0d28b32.png">


> Lembrar que o FROM vc usa para a base de dados principal e INNR JOIN para a segunda base de dados 

### INNER JOIN - 3 TABLES

We've seen how to join 2 tables together - album with track, and album with artist. In this exercise, you'll join all three tables to pull together a more complete result set. You'll continue using INNER JOIN, but you need to specify more than one.

Here, note that because both track and artist contain a name column, you need to qualify where you are selecting the columns by prefixing the column name with the relevant table name.

INSTRUCTIONS

+ Qualify the `name` column by specifying the correct table prefix in both cases.
+ Complete both `INNER JOIN` clauses to join `album` with `track`, and `artist` with `album`.

```sql
SELECT track_id,
-- Enter the correct table name prefix when retrieving the name column from the track table
  track.name AS track_name,
  title as album_title,
  -- Enter the correct table name prefix when retrieving the name column from the artist table
  artist.name AS artist_name
FROM track 
  -- Complete the matching columns to join album with track, and artist with album
INNER JOIN album 
ON track.album_id = album.album_id 
INNER JOIN artist 
ON album.artist_id = artist.artist_id;
```

<img width="981" alt="image" src="https://user-images.githubusercontent.com/68601128/120907561-04bf1800-c639-11eb-81b3-f56a35fb6ea0.png">

### LEFT AND RIGHT JOIN

<img width="534" alt="image" src="https://user-images.githubusercontent.com/68601128/120928962-590bdb80-c6bd-11eb-9034-7f56647c012a.png">

Example

<img width="872" alt="image" src="https://user-images.githubusercontent.com/68601128/120928991-8ce70100-c6bd-11eb-81e0-7c7d759cf6ef.png">

5. LEFT JOIN SYNTAX

Here's how we would perform a LEFT join with these tables. We can also see a pictorial representation of the join below. The 'Admitted' table is on the LEFT of the join, 'Discharged' is on the right, and they are joined by the Patient_ID. The symbol on the connecting line indicates that ALL rows will be returned from the Admitted table.
6. LEFT JOIN results

Here we see the final results of the query. We can clearly see the matching records. Patients 2 and 5, who have not yet been discharged, are identified by NULLs in the Discharged column.
7. RIGHT JOIN

RIGHT JOINS are similar to LEFT joins. The difference is that all rows from the right hand table are returned, plus any matches from the left hand table. Any non-matched rows in the left hand table will return a NULL value. 

<img width="574" alt="image" src="https://user-images.githubusercontent.com/68601128/120933240-91b4b080-c6cf-11eb-936d-4f1f04b47871.png">

<img width="636" alt="image" src="https://user-images.githubusercontent.com/68601128/120933254-9f6a3600-c6cf-11eb-960b-683ae6662c2f.png">

<img width="863" alt="image" src="https://user-images.githubusercontent.com/68601128/120933275-bd379b00-c6cf-11eb-8741-5723ba295e7a.png">

Hint

+ The most common type of join is one that returns rows that match and discards non-matching rows
+ Fully qualified column names begin with the table name, then a period (without any space) and then the column name

RIGHT JOIN EXAMPLE

INSTRUCTIONS 1.1 

Let's now try some RIGHT joins. A RIGHT join will return all rows from the right hand table, plus any matches from the left hand side table.

In addition to performing a RIGHT join, you'll also learn how to avoid problems when different tables have the same column names, by fully qualifying the column in your select statement. Remember, we do this by prefixing the column name with the table name.

For this exercise, we'll return to the Chinook database from earlier in the chapter.

+ SELECT the fully qualified column names album_id from album and name from artist. Then, join the tables so that only matching rows are returned (non-matches should be discarded).

```sql 
-- SELECT the fully qualified album_id column from the album table
SELECT 
  album.album_id,
  title,
  album.artist_id,
  -- SELECT the fully qualified name column from the artist table
  artist.name as artist
FROM album
-- Perform a join to return only rows that match from both tables
INNER JOIN artist ON album.artist_id = artist.artist_id
WHERE album.album_id IN (213,214)
```

<img width="981" alt="image" src="https://user-images.githubusercontent.com/68601128/121423404-9afb8280-c946-11eb-95be-edaed2f9de6f.png">

INSTRUCTIONS 1.2

+ To complete the query, join the album table to the track table using the relevant fully qualified album_id column. The album table is on the left-hand side of the join, and the additional join should return all matches or NULLs.

```SQL
SELECT 
  album.album_id,
  title,
  album.artist_id,
  artist.name as artist
FROM album
INNER JOIN artist ON album.artist_id = artist.artist_id
-- Perform the correct join type to return matches or NULLS from the track table
RIGHT JOIN track on album.album_id = track.album_id
WHERE album.album_id IN (213,214)
```

<img width="828" alt="image" src="https://user-images.githubusercontent.com/68601128/121424901-380aeb00-c948-11eb-9102-085a58b264d1.png">
