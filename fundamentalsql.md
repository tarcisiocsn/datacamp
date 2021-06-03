# SQL 

## TIPS

**Filtering Results**
```sql

    = equal
    <> not equal
    < less than
    > greater than
    <= less than or equal to
    >= greater than or equal to
```

**SELECT DISTINCT**

Often your results will include many duplicate values. If you want to select all the unique values from a column, you can use the DISTINCT keyword.
This might be useful if, for example, you're interested in knowing which languages are represented in the films table:

```SQL
SELECT DISTINCT language
FROM films;
```
**PRACTICE WITH COUNT**

As you've seen, COUNT(*) tells you how many rows are in a table. However, if you want to count the number of non-missing values in a particular column, you can call COUNT on just that column.

For example, to count the number of birth dates present in the people table:

```SQL
SELECT COUNT(birthdate)
FROM people;
```
It's also common to combine COUNT with DISTINCT to count the number of distinct values in a column.

For example, this query counts the number of distinct birth dates contained in the `people` table:

```SQL
SELECT COUNT(DISTINCT birthdate)
FROM people;
```
> Count the number of unique countries in the films table.
```SQL
SELECT COUNT(DISTINCT country)
FROM films; 
```

**WHERE ARE**

```SQL 
SELECT title
FROM films
WHERE release_year > 1994
AND release_year < 2000;

-- OR

SELECT title
FROM films
WHERE release_year > 1994 AND < 2000; 

```
OR

```SQL 
SELECT title, release_year
FROM films
WHERE language = 'Spanish' AND release_year < 2000; 

```

Nice example: Get all details for Spanish language films released after 2000, but before 2010.

```sql 
SELECT *
FROM films
WHERE language = 'Spanish' 
AND release_year > 2000 
AND release_year < 2010;

```

**WHERE AND OR**

What if you want to select rows based on multiple conditions where some but not all of the conditions need to be met? For this, SQL has the OR operator.
You now know how to select rows that meet some but not all conditions by combining **AND** and **OR**.

For example, the following returns all films released in either 1994 or 2000:

```SQL 
SELECT title
FROM films
WHERE release_year = 1994
OR release_year = 2000;

```

When combining AND and OR, be sure to enclose the individual clauses in parentheses, like so:

```SQL
SELECT title
FROM films
WHERE (release_year = 1994 OR release_year = 1995)
AND (certification = 'PG' OR certification = 'R');
```

For example, the following query selects all films that were released in 1994 or 1995 which had a rating of PG or R

```SQL 
SELECT title
FROM films
WHERE (release_year = 1994 OR release_year = 1995)
AND (certification = 'PG' OR certification = 'R');
```
Now you'll write a query to get the title and release year of films released in the 90s which were in French or Spanish and which took in more than $2M gross.

```sql 

SELECT title, release_year
FROM films
WHERE (release_year >= 1990 AND release_year < 2000)
AND (language = 'French' OR language = 'Spanish')
AND gross > 2000000;
-- gross é receita bruta
```

**BETWEEN**

Checking for ranges like this is very common, so in SQL the BETWEEN keyword provides a useful shorthand for filtering values within a specified range. 
This query is equivalent to the one above:
```sql
SELECT title
FROM films
WHERE release_year
BETWEEN 1994 AND 2000;
```
ps. It's important to remember that BETWEEN is inclusive, meaning the beginning and end values are included in the results!

For example, suppose we have a table called kids. We can get the names of all kids between the ages of 2 and 12 from the United States:

```sql 
SELECT name
FROM kids
WHERE age BETWEEN 2 AND 12
AND nationality = 'USA';
```

**WHERE IN**

As you've seen, WHERE is very useful for filtering results. However, if you want to filter based on many conditions, WHERE can get unwieldy. For example:

```SQL 
SELECT name
FROM kids
WHERE age = 2
OR age = 4
OR age = 6
OR age = 8
OR age = 10;
```

Enter the IN operator! The IN operator allows you to specify multiple values in a WHERE clause, making it easier and quicker to specify multiple OR conditions! Neat, right?
So, the above example would become simply:

```SQL 
SELECT name
FROM kids
WHERE age IN (2, 4, 6, 8, 10);
```

Get the title and release year of all films released in 1990 or 2000 that were longer than two hours. Remember, duration is in minutes!

```sql 
SELECT title, release_year
FROM films
WHERE release_year IN (1990, 2000)
AND duration > 120; 
```
Get the title and language of all films which were in English, Spanish, or French.

```sql 
SELECT title, language 
FROM films
WHERE language IN ('English', 'Spanish', 'French');
```
**INTRODUCTION TO NULL AND NOT NULL**

In SQL, NULL represents a missing or unknown value. You can check for NULL values using the expression ``IS NULL``. For example, to count the number of missing birth dates in the people table:

```sql 
SELECT COUNT(*)
FROM people
WHERE birthdate IS NULL;
```

Sometimes, you'll want to filter out missing values so you only get results which are not NULL. To do this, you can use the IS NOT NULL operator.

For example, this query gives the names of all people whose birth dates are not missing in the people table.

```sql 
SELECT name
FROM people
WHERE birthdate IS NOT NULL;
```
**LIKE AND NOT LIKE**

As you've seen, the WHERE clause can be used to filter text data. However, so far you've only been able to filter by specifying the exact text you're interested in. In the real world, often you'll want to search for a pattern rather than a specific text string.

In SQL, the LIKE operator can be used in a WHERE clause to search for a pattern in a column. To accomplish this, you use something called a wildcard as a placeholder for some other values. There are two wildcards you can use with LIKE:

The ``%`` wildcard will match zero, one, or many characters in text. For example, the following query matches companies like ``'Data'``, ``'DataC'``, ``'DataCamp'``, ``'DataMind'``, and so on:

```SQL 
SELECT name
FROM companies
WHERE name LIKE 'Data%';
```
The ``_`` wildcard will match a single character. For example, the following query matches companies like ``'DataCamp'``, ``'DataComp'``, and so on:

```SQL
SELECT name
FROM companies
WHERE name LIKE 'DataC_mp';
```

PS. You can also use the ``NOT LIKE`` operator to find records that don't match the pattern you specify.

> Get the names of all people whose names begin with 'B'. The pattern you need is 'B%'.

```SQL 
SELECT name
FROM people 
WHERE name LIKE 'B%'; 
```
> Get the names of people whose names have 'r' as the second letter. The pattern you need is '_r%'.

```sql 
SELECT name
FROM people
WHERE name LIKE '_r%';
```
> Get the names of people whose names don't start with A. The pattern you need is 'A%'.

```sql 
SELECT name
FROM people 
WHERE name NOT LIKE 'A%'; 
```

**AGGREGATE FUNCTIONS**

Often, you will want to perform some calculation on the data in a database. SQL provides a few functions, called aggregate functions, to help you out with this.

For example,

```sql 
SELECT AVG(budget)
FROM films;

```

gives you the `average` value from the budget column of the films table. Similarly, the `MAX` function returns the highest budget:

```sql 
SELECT MAX(budget)
FROM films;
```
The `SUM` function returns the result of adding up the numeric values in a column:

```SQL
SELECT SUM(budget)
FROM films;

```

PS. You can probably guess what the MIN function does! Now it's your turn to try out some SQL functions. ;)

> Use the `SUM` function to get the total duration of all films.

```sql
SELECT SUM(duration)
FROM films; 
```

> Get the average duration of all films.

```sql 
SELECT AVG(duration)
FROM films;

```

> Get the duration of the shortest film.

```sql 
SELECT MIN(duration)
FROM films;
```

> Get the amount grossed by the worst performing film.

```sql
SELECT MIN(gross)
FROM films;

```

**Combining aggregate functions with WHERE**

ggregate functions can be combined with the WHERE clause to gain further insights from your data.

For example, to get the total budget of movies made in the year 2010 or later:

```sql
SELECT SUM(budget)
FROM films
WHERE release_year >= 2010;
```

> Get the average amount grossed by all films whose titles start with the letter 'A'.

```sql
SELECT AVG(gross)
FROM films
WHERE title LIKE 'A%'
```

> Get the amount grossed by the worst performing film in 1994.

```sql 
SELECT MIN(gross)
FROM films
WHERE release_year = 1994
-- pior rendimento na bilheteria
```
> Get the amount grossed by the best performing film between 2000 and 2012, inclusive.

```SQL
SELECT MAX(gross)
FROM films
WHERE release_year BETWEEN 2000 AND 2012
```

**N NOTE ON ARITHMETIC**

In addition to using aggregate functions, you can perform basic arithmetic with symbols like `+`, `-`, `*`, and `/`.

So, for example, this gives a result of 12:

```SQL
SELECT (4 * 3);
```

However, the following gives a result of 1:

```SQL
SELECT (4 / 3);
```
> What's going on here?
> SQL assumes that if you divide an integer by an integer, you want to get an integer back. So be careful when dividing!

If you want more precision when dividing, you can add decimal places to your numbers. For example,

```SQL
SELECT (4.0 / 3.0) AS result;
```
gives you the result you would expect: `1.333`.

**IT'S AS SIMPLE AS ALIASING** 

You may have noticed in the first exercise of this chapter that the column name of your result was just the name of the function you used. For example,

```SQL 
SELECT MAX(budget)
FROM films;
```
gives you a result with one column, named max. But what if you use two functions like this?

```SQL
SELECT MAX(budget), MAX(duration)
FROM films;

```
OUTPUT

<img width="678" alt="image" src="https://user-images.githubusercontent.com/68601128/120119198-bc9d8280-c16c-11eb-9696-1109cde8993d.png">

Well, then you'd have two columns named max, which isn't very useful!

To avoid situations like this, SQL allows you to do something called aliasing. Aliasing simply means you assign a temporary name to something. To alias, you use the `AS` keyword, which you've already seen earlier in this course.

For example, in the above example we could use aliases to make the result clearer:

```SQL
SELECT MAX(budget) AS max_budget,
       MAX(duration) AS max_duration
FROM films;
```
OUPUT

<img width="501" alt="image" src="https://user-images.githubusercontent.com/68601128/120119255-1605b180-c16d-11eb-83b5-8e97d346473b.png">

Aliases are helpful for making results more readable!

> Get the title and net profit (the amount a film grossed, minus its budget) for all films. Alias the net profit as net_profit.

```sql 
SELECT title, (gross - budget) AS net_profit
FROM films; 

-- nesse caso pode dar até net_profit negativo
```
> Get the title and duration in hours for all films. The duration is in minutes, so you'll need to divide by 60.0 to get the duration in hours. Alias the duration in hours as duration_hours.

```sql 
SELECT title, duration/60.0 AS duration_hours
FROM films; 
```
OUTPUT

<img width="730" alt="image" src="https://user-images.githubusercontent.com/68601128/120119398-e905ce80-c16d-11eb-8e93-592868c3288c.png">

> Get the average duration in hours for all films, aliased as avg_duration_hours.

```sql
SELECT AVG(duration)/60.0 AS avg_duration_hours
FROM films
```

OUTPUT

<img width="293" alt="image" src="https://user-images.githubusercontent.com/68601128/120119446-1f434e00-c16e-11eb-9043-926813b71d08.png">

> Get the percentage of people who are no longer alive. Alias the result as percentage_dead. Remember to use 100.0 and not 100!

```sql 
-- get the count(deathdate) and multiply by 100.0
-- then divide by count(*)

SELECT COUNT(deathdate) * 100.0 / COUNT(*) AS percentage_dead
FROM people
```

> Get the number of years between the newest film and oldest film. Alias the result as difference.

```sql 
SELECT MAX(release_year) - MIN(release_year) AS difference
FROM films; 
```
OUTPUT

<img width="112" alt="image" src="https://user-images.githubusercontent.com/68601128/120119689-84e40a00-c16f-11eb-8f89-4dd471236768.png">

> Get the number of decades the films table covers. Alias the result as number_of_decades. The top half of your fraction should be enclosed in parentheses.

```sql
SELECT (MAX(release_year) - MIN(release_year)) / 10.0
AS number_of_decades
FROM films;
```

**ORDER BY** 

In this chapter you'll learn how to sort and group your results to gain further insight. Let's go!

In SQL, the `ORDER BY` keyword is used to sort results in ascending or descending order according to the values of one or more columns. 

By default `ORDER BY` will sort in ascending order. If you want to sort the results in descending order, you can use the `DESC` keyword. For example,

```SQL
SELECT title
FROM films
ORDER BY release_year DESC;
```
gives you the titles of films sorted by release year, from newest to oldest.

> Get the names of people from the people table, sorted alphabetically.

```sql 
SELECT name
FROM people
ORDER BY name; 
```

> Get the names of people, sorted by birth date.

```sql 
SELECT name
FROM people
ORDER BY birthdate; 
```
> Get the birth date and name for every person, in order of when they were born.

```sql 
SELECT birthdate, name
FROM people
ORDER BY birthdate;
```

> Get the title of films released in 2000 or 2012, in the order they were released.

```sql
SELECT title
FROM films
WHERE (release_year = 2000 OR release_year = 2012)
ORDER BY release_year
```

> Get all details for all films except those released in 2015 and order them by duration.

```sql
SELECT *
FROM films
WHERE release_year <> 2015
ORDER BY duration; 

```
> Get the title and gross earnings for movies which begin with the letter 'M' and order the results alphabetically.

```sql 
SELECT title, gross
FROM films
WHERE title LIKE 'M%'
ORDER BY title; 
```
> Get the IMDB score and film ID for every film from the reviews table, sorted from highest to lowest score.

```sql 
SELECT imdb_score, film_id
FROM reviews
ORDER BY imdb_score DESC;
```
**SORTING MULTIPLE COLUMNS**

ORDER BY can also be used to sort on multiple columns. It will sort by the first column specified, then sort by the next, then the next, and so on. For example,

```SQL
SELECT birthdate, name
FROM people
ORDER BY birthdate, name;
```
sorts on birth dates first (oldest to newest) and then sorts on the names in alphabetical order. The order of columns is important!

> Get the birth date and name of people in the people table, in order of when they were born and alphabetically by name.

```sql
SELECT birthdate, name
FROM people
ORDER BY birthdate, name;

```

**GROUP BY**

For example, you might want to count the number of male and female employees in your company. Here, what you want is to group all the males together and count them, and group all the females together and count them. In SQL, GROUP BY allows you to group a result by one or more columns, like so:

```SQL
SELECT sex, count(*)
FROM employees
GROUP BY sex;
```
OUTPUT

<img width="874" alt="image" src="https://user-images.githubusercontent.com/68601128/120124286-13658500-c18a-11eb-9e53-a20cb869715b.png">

Commonly, GROUP BY is used with aggregate functions like COUNT() or MAX(). Note that GROUP BY always goes after the FROM clause!

Note that you can combine `GROUP BY` with `ORDER BY` to group your results, calculate something about them, and then order your results. For example,

OUTPUT

<img width="485" alt="image" src="https://user-images.githubusercontent.com/68601128/120124354-7525ef00-c18a-11eb-9d95-9614f6ac929e.png">

because there are more females at our company than males. `Note also that ORDER BY always goes after GROUP BY`. Let's try some exercises!

> Get the release year and count of films released in each year.

```SQL 
SELECT release_year, count(*)
FROM films
GROUP BY release_year; 
```
<img width="744" alt="image" src="https://user-images.githubusercontent.com/68601128/120124463-ed8cb000-c18a-11eb-87f8-993fd8f29609.png">

> Get the release year and average duration of all films, grouped by release year.

```SQL
SELECT release_year, AVG(duration)
FROM films
GROUP BY release_year;
```
OUTPUT

<img width="737" alt="image" src="https://user-images.githubusercontent.com/68601128/120124593-786daa80-c18b-11eb-9c0d-fd6de11e8c9b.png">

> Get the release year and largest budget for all films, grouped by release year.

```sql
SELECT release_year, MAX(budget)
FROM films
GROUP BY release_year;
```
> Get the IMDB score and count of film reviews grouped by IMDB score in the reviews table.

```sql 
SELECT imdb_score, COUNT(*)
FROM reviews
GROUP BY imdb_score;
```
OUTPUT

<img width="748" alt="image" src="https://user-images.githubusercontent.com/68601128/120124693-f336c580-c18b-11eb-9927-56f55a4610c8.png">

PS. Make sure to always put the ORDER BY clause at the end of your query. You can't sort values that you haven't calculated yet!

> Get the release year and lowest gross earnings per release year.

```sql 
SELECT release_year, MIN(gross)
FROM films
GROUP BY release_year;
```
OUTPUT

<img width="741" alt="image" src="https://user-images.githubusercontent.com/68601128/120124894-d5b62b80-c18c-11eb-92a7-88b819037c58.png">

> Get the language and total gross amount films in each language made.

```sql
SELECT language, SUM(gross)
FROM films
GROUP BY language;
```
OUTPUT

<img width="744" alt="image" src="https://user-images.githubusercontent.com/68601128/120124957-131ab900-c18d-11eb-983a-f261affe131b.png">

> Get the release year, country, and highest budget spent making a film for each year, for each country. Sort your results by release year and country.

```sql 
SELECT release_year, country, MAX(budget)
FROM films
GROUP BY release_year, country
ORDER BY release_year, country; 
```
OUTPUT

<img width="754" alt="image" src="https://user-images.githubusercontent.com/68601128/120125123-c1266300-c18d-11eb-8a1c-b3dfae32068d.png">

> Get the country, release year, and lowest amount grossed per release year per country. Order your results by country and release year.

```sql
SELECT country, release_year, MIN(gross)
FROM films
GROUP BY release_year, country
ORDER BY country, release_year;
```
<img width="757" alt="image" src="https://user-images.githubusercontent.com/68601128/120125177-fc289680-c18d-11eb-8235-d21bf6a113e2.png">

**HAVING** 

PS. In SQL, aggregate functions can't be used in WHERE clauses. For example, the following query is invalid:
PS. Quando voce quiser usar o where, mas queria que fosse o statement de AVG, MAX, MIN, COUNT por exemplo, terá que usar o HAVING

```SQL
--DARÁ INVÁLIDO
SELECT release_year
FROM films
GROUP BY release_year
WHERE COUNT(title) > 10;
```
This means that if you want to filter based on the result of an aggregate function, you need another way! That's where the HAVING clause comes in. For example,

```SQL
SELECT release_year
FROM films
GROUP BY release_year
HAVING COUNT(title) > 10;
```
`shows only those years in which more than 10 films were released.`

> In how many different years were more than 200 movies released?

```SQL
SELECT release_year
FROM films
GROUP BY release_year
HAVING COUNT(title) > 200;
```
<img width="756" alt="image" src="https://user-images.githubusercontent.com/68601128/120125453-4100fd00-c18f-11eb-9a9d-4acdabdc6a48.png">

>Modify your query so that only years with an average budget of greater than $60 million are included.

```sql 
SELECT release_year, AVG(budget) AS avg_budget, AVG(gross) AS avg_gross
FROM films
WHERE release_year > 1990 
GROUP BY release_year
HAVING AVG(budget) > 60000000;
```

OUTPUT

<img width="739" alt="image" src="https://user-images.githubusercontent.com/68601128/120205632-8f9aaf80-c200-11eb-828d-06b447eed93a.png">

> Finally, modify your query to order the results from highest average gross earnings to lowest.

```SQL
SELECT release_year, AVG(budget) AS avg_budget, AVG(gross) AS avg_gross
FROM films
WHERE release_year > 1990
GROUP BY release_year
HAVING AVG(budget) > 60000000
ORDER BY AVG(gross) DESC;
```

OUTPUT

<img width="757" alt="image" src="https://user-images.githubusercontent.com/68601128/120205803-c07ae480-c200-11eb-8cf9-de08fa0ba11b.png">


**EXTRA**

Get the country, average budget, and average gross take of countries that have made more than 10 films. Order the result by country name, and limit the number of results displayed to 5. You should alias the averages as avg_budget and avg_gross respectively.

```sql 
-- select country, average budget, 
--     and average gross
SELECT country, AVG(budget) AS avg_budget, AVG(gross) AS avg_gross
-- from the films table
FROM films
-- group by country 
GROUP BY country
-- where the country has more than 10 titles
HAVING COUNT(country) > 10
-- order by country
ORDER BY country
-- limit to only show 5 results
LIMIT 5; 
```

<img width="752" alt="image" src="https://user-images.githubusercontent.com/68601128/120206317-721a1580-c201-11eb-932e-670ef907b15c.png">


**INTRODUCTION TO INNER JOIN**

<img width="436" alt="image" src="https://user-images.githubusercontent.com/68601128/120208615-100edf80-c204-11eb-8e79-206d06161569.png">

```sql 
SELECT *
FROM left_table
INNER JOIN right_table
ON left_table.id = right_table.id;
```

Real Example:

```sql
SELECT p1.country, p1.continent, prime_minister, president
FROM prime_ministers AS p1
INNER JOIN presidents AS p2 
ON p1.country = p2.country;
```
OUTPUT

<img width="577" alt="image" src="https://user-images.githubusercontent.com/68601128/120209094-a7743280-c204-11eb-910a-7abd95fc6a80.png">

Throughout this course, you'll be working with the `countries` database containing information about the most populous world cities as well as country-level economic data, population data, and geographic data. This `countries` database also contains information on languages spoken in each country.

You can see the different tables in this database by clicking on the tabs on the bottom right below query.sql. Click through them to get a sense for the types of data that each table contains before you continue with the course! Take note of the fields that appear to be shared across the tables.

<img width="746" alt="image" src="https://user-images.githubusercontent.com/68601128/120210404-1f8f2800-c206-11eb-8aba-4aa1b2c033b1.png">

You'll start off with a SELECT statement and then build up to an inner join with the `cities` and `countries` tables. Let's get to it!

> `cities` table 

<img width="747" alt="image" src="https://user-images.githubusercontent.com/68601128/120211091-e99e7380-c206-11eb-985c-aec31d3b0d73.png">

> `countries` table

<img width="887" alt="image" src="https://user-images.githubusercontent.com/68601128/120211170-033fbb00-c207-11eb-921c-9082d23efe49.png">



Instructions 1

+ Inner join the `cities` table on the left to the `countries` table on the right, keeping all of the fields in both tables.
+ You should match the tables on the `country_code` field in `cities` and the `code` field in `countries.`
+ Do not alias your tables here or in the next step. Using `cities` and `countries` is fine for now.

```sql
SELECT * 
FROM cities
  -- 1. Inner join to countries
  INNER JOIN countries
    -- 2. Match on the country codes
    ON cities.country_code = countries.code;
```

OUTPUT

<img width="1213" alt="image" src="https://user-images.githubusercontent.com/68601128/120215464-23be4400-c20c-11eb-8f7e-19e73b98aae8.png">


Instructions 2

+ Modify the SELECT statement to keep only the name of the city, the name of the country, and the name of the region the country resides in.

+ Recall from our Intro to SQL for Data Science course that you can alias fields using AS. Alias the name of the city AS city and the name of the country AS country.

```sql 
-- 1. Select name fields (with alias) and region 
SELECT cities.name AS city, countries.name AS country, region
FROM cities
  INNER JOIN countries
    ON cities.country_code = countries.code;
```
OUTPUT

<img width="878" alt="image" src="https://user-images.githubusercontent.com/68601128/120216143-076ed700-c20d-11eb-8e51-7ab68ff84958.png">

**GENERAL RULE INNER JOIN**

```SQL
SELECT c1.name AS city, c2.name AS country
FROM cities AS c1
INNER JOIN countries AS c2
ON c1.country_code = c2.code;
```
Notice that to select a field in your query that appears in multiple tables, you'll need to identify which table/table alias you're referring to by using a . in your SELECT statement. (É UM EXEMPLO COM A TABELA CITIES E COUNTRIES QUE TEM O MESMO `NAME`PARA DIFERENTES PARTES, LOGO, VOCÊ COLOCA  `AS` PARA DIFERENCIAR OS 2)

You'll now explore a way to get data from both the `countries` and `economies` tables to examine the inflation rate for both 2010 and 2015.

<img width="1217" alt="image" src="https://user-images.githubusercontent.com/68601128/120216450-6af90480-c20d-11eb-8bcb-19d935470b1e.png">

<img width="1225" alt="image" src="https://user-images.githubusercontent.com/68601128/120216465-72201280-c20d-11eb-8cab-f39430f44bdc.png">

And `population` table

<img width="1128" alt="image" src="https://user-images.githubusercontent.com/68601128/120234384-36e20b80-c22e-11eb-9922-e27d592bf55a.png">


Instructions

+ Join the tables `countries` (left) and `economies` (right) aliasing `countries AS c` and `economies AS e`.

+ Specify the field to match the tables `ON`.

+ From this join, `SELECT`:

···`c.code`, aliased as `country_code`.··
···`name`, `year`, and `inflation_rate`, not aliased.··

```sql
-- 3. Select fields with aliases
SELECT c.code AS country_code, name, year, inflation_rate
FROM countries AS c
  -- 1. Join to economies (alias e)
  INNER JOIN economies AS e
    -- 2. Match on code
    ON c.code = e.code;
```

OUTPUT

<img width="777" alt="image" src="https://user-images.githubusercontent.com/68601128/120217549-e0190980-c20e-11eb-91b8-59684e996dc4.png">

INSTRUCTIONS

+ Inner join countries (left) and populations (right) on the code and country_code fields respectively.

+ Alias countries AS c and populations AS p.

+ Select code, name, and region from countries and also select year and fertility_rate from populations (5 fields in total).

```SQL 
-- 4. Select fields
SELECT code, name, region, year, fertility_rate
  -- 1. From countries (alias as c)
  FROM countries AS c
  -- 2. Join with populations (as p)
  INNER JOIN populations as p
    -- 3. Match on country code
    ON c.code = p.country_code; 
```

OUTPUT

<img width="874" alt="image" src="https://user-images.githubusercontent.com/68601128/120234486-714ba880-c22e-11eb-990e-d4fc2fb10f00.png">

INSTRUCTIONS

+ Add an additional inner join with economies to your previous query by joining on code.

+ Include the unemployment_rate column that became available through joining with economies.

+ Note that year appears in both populations and economies, so you have to explicitly use e.year instead of year as you did before.

```SQL 
-- 6. Select fields
SELECT c.code, name, region, e.year, fertility_rate, unemployment_rate
  -- 1. From countries (alias as c)
  FROM countries AS c
  -- 2. Join to populations (as p)
  INNER JOIN populations AS p
    -- 3. Match on country code
    ON c.code = p.country_code
  -- 4. Join to economies (as e)
  INNER JOIN economies AS e
    -- 5. Match on country code
    ON c.code = e.code;
```
OUTPUT

<img width="873" alt="image" src="https://user-images.githubusercontent.com/68601128/120234509-81fc1e80-c22e-11eb-8dd4-de131c1d5d64.png">

INSTRUCTIONS

+ Scroll down the query result and take a look at the results for Albania from your previous query. Does something seem off to you?

+ The trouble with doing your last join on c.code = e.code and not also including year is that e.g. the 2010 value for fertility_rate is also paired with the 2015 value for unemployment_rate.

+ Fix your previous query: in your last ON clause, use AND to add an additional joining condition. In addition to joining on code in c and e, also join on year in e and p.

```SQL
-- 6. Select fields
SELECT c.code, name, region, e.year, fertility_rate, unemployment_rate
  -- 1. From countries (alias as c)
  FROM countries AS c
  -- 2. Join to populations (as p)
  INNER JOIN populations AS p
    -- 3. Match on country code
    ON c.code = p.country_code
  -- 4. Join to economies (as e)
  INNER JOIN economies AS e
    -- 5. Match on country code and year
    ON c.code = e.code AND e.year = p.year; 
```

OUTPUT

<img width="873" alt="image" src="https://user-images.githubusercontent.com/68601128/120234596-ba036180-c22e-11eb-95bf-667a85e749e2.png">


**INNER JOIN via USING** 

Usa USING quando os nomes das tabelas são iguais, como no exemplo

<img width="651" alt="image" src="https://user-images.githubusercontent.com/68601128/120234798-11093680-c22f-11eb-9605-e4036a421737.png">

When joining tables with a common field name, e.g.

```SQL 
SELECT *
FROM countries
  INNER JOIN economies
    ON countries.code = economies.code
   
```
You can use USING as a shortcut:

```sql
SELECT *
FROM countries
  INNER JOIN economies
    USING(code)
```
You'll now explore how this can be done with the `countries` and `languages` tables.

INSTRUCTIONS

+ Inner join countries on the left and languages on the right with USING(code).

+ select the fields corresponding to:

1.country name AS country,

2.continent name,

3.language name AS language, and

4.whether or not the language is official.

+ Remember to alias your tables using the first letter of their names.

```SQL
-- 4. Select fields
SELECT c.name AS country, continent, l.name AS language, official
  -- 1. From countries (alias as c)
  FROM countries AS c 
  -- 2. Join to languages (as l)
  INNER JOIN languages AS l
    -- 3. Match using code
    USING(code)
```
OUTPUT

<img width="737" alt="image" src="https://user-images.githubusercontent.com/68601128/120236260-3b102800-c232-11eb-843e-9a48126d919c.png">

**SELF-JOIN**

Self-joins are used to compare values in a field to other values of the same field from within the same table.

What if you wanted to create a new table showing countries that are in the same continent matched as pairs? Let's explore a chunk of INNER JOIN code using the prime_ministers table. 

<img width="577" alt="image" src="https://user-images.githubusercontent.com/68601128/120241584-7104da80-c239-11eb-8d68-a04ee7653519.png">

<img width="715" alt="image" src="https://user-images.githubusercontent.com/68601128/120251100-cdc2be00-c256-11eb-8220-b82031f28d89.png">

**CASE WHEN and THEN**

<img width="581" alt="image" src="https://user-images.githubusercontent.com/68601128/120251632-89d0b880-c258-11eb-9755-8a274c7b5ac7.png">


CASE is a way to do multiple `if-then-else` statements in a simplified way in SQL. 

<img width="601" alt="image" src="https://user-images.githubusercontent.com/68601128/120251606-71f93480-c258-11eb-8f4e-5fd19f25e8b3.png">

You can now see the basic layout for creating a new field containing the groupings. How might we fill them in? After the first WHEN should specify that we want to check for indep_year being less than 1900. Next we want indep_year_group to contain 'between 1900 and 1930' in the next blank. Lastly any other record not matching these conditions will be assigned the value of 'after 1930' for indep_year_group. 

Check out the completed query with completed blanks. Notice how the values of indep_year are grouped in indep_year_group. Also observe how continent relates to indep_year_group. 

<img width="596" alt="image" src="https://user-images.githubusercontent.com/68601128/120251664-a40a9680-c258-11eb-9f13-6f1eb5c0d579.png">

**SELF-JOIN EXAMPLES**

In this exercise, you'll use the `populations` table to perform a self-join to calculate the percentage increase in population from 2010 to 2015 for each country code!

Since you'll be joining the populations table to itself, you can alias populations as `p1` and also `populations` as `p2`. This is good practice whenever you are aliasing and your tables have the same first letter. Note that you are required to alias the tables with self-joins.

INSTRUCTION 1.1

> Population Table

<img width="748" alt="image" src="https://user-images.githubusercontent.com/68601128/120252284-758dbb00-c25a-11eb-831b-d1a76ddc3291.png">

+ Join populations with itself ON country_code.

+ select the country_code from p1 and the size field from both p1 and p2. SQL won't allow same-named fields, so alias p1.size as size2010 and p2.size as size2015.

```SQL
-- 4. Select fields with aliases
SELECT p1.country_code, p1.size AS size2010, p2.size AS size2015
-- 1. From populations (alias as p1)
FROM populations AS p1
  -- 2. Join to itself (alias as p2)
  INNER JOIN populations AS p2
    -- 3. Match on country code
    ON p1.country_code = p2.country_code
```

OUTPUT

<img width="750" alt="image" src="https://user-images.githubusercontent.com/68601128/120251994-986b9f80-c259-11eb-9677-043cca7a34df.png">

INSTRUCTION 1.2

Notice from the result that for each country_code you have four entries laying out all combinations of 2010 and 2015.

+ Extend the ON in your query to include only those records where the p1.year (2010) matches with p2.year - 5 (2015 - 5 = 2010). This will omit the three entries per country_code that you aren't interested in.

```SQL 
-- 5. Select fields with aliases
SELECT p1.country_code,
       p1.size AS size2010,
       p2.size AS size2015
-- 1. From populations (alias as p1)
FROM populations as p1
  -- 2. Join to itself (alias as p2)
  INNER JOIN populations as p2
    -- 3. Match on country code
    ON p1.country_code = p2.country_code
        -- 4. and year (with calculation)
       AND p1.year = p2.year - 5; 
```

<img width="751" alt="image" src="https://user-images.githubusercontent.com/68601128/120252702-ade1c900-c25b-11eb-8b87-1e6279539b09.png">

INSTRUCTION 1.3

<img width="472" alt="image" src="https://user-images.githubusercontent.com/68601128/120252756-cd78f180-c25b-11eb-85ec-a8ad48e42972.png">


``` SQL
SELECT p1.country_code,
       p1.size AS size2010, 
       p2.size AS size2015,
       -- 1. calculate growth_perc
       ((p2.size - p1.size)/p1.size * 100.0) AS growth_perc
-- 2. From populations (alias as p1)
FROM populations AS p1
  -- 3. Join to itself (alias as p2)
  INNER JOIN populations AS p2
    -- 4. Match on country code
    ON p1.country_code = p2.country_code
        -- 5. and year (with calculation)
        AND p1.year = p2.year - 5;
```
OUTPUT

<img width="811" alt="image" src="https://user-images.githubusercontent.com/68601128/120252783-e2558500-c25b-11eb-8f20-b98e69f72dc6.png">

**CASE WHEN AND THEN EXAMPLES**

Often it's useful to look at a numerical field not as raw data, but instead as being in different categories or groups.

You can use CASE with `WHEN`, `THEN`, `ELSE`, and `END` to define a new grouping field.

INSTRUCTIONS

Using the countries table, create a new field AS geosize_group that groups the countries into three groups:

+ If `surface_area` is greater than 2 million, `geosize_group` is `'large'`.
+ If `surface_area` is greater than 350 thousand but not larger than 2 million, `geosize_group` is `'medium'`.
+ Otherwise, geosize_group is `'small'`.

```SQL
SELECT name, continent, code, surface_area,
    -- 1. First case
    CASE WHEN surface_area > 2000000 THEN 'large'
        -- 2. Second case
        WHEN  surface_area > 350000 THEN 'medium'
        -- 3. Else clause + end
        ELSE 'small' END
        -- 4. Alias name
        AS geosize_group
-- 5. From table
FROM countries;
```
OUTPUT

<img width="746" alt="image" src="https://user-images.githubusercontent.com/68601128/120253218-2c8b3600-c25d-11eb-8900-1f74975149df.png">

**INNER CHALLENGE**

The table you created with the added `geosize_group` field has been loaded for you here with the name `countries_plus`. Observe the use of (and the placement of) the `INTO` command to create this countries_plus table:

```SQL
SELECT name, continent, code, surface_area,
    CASE WHEN surface_area > 2000000
            THEN 'large'
       WHEN surface_area > 350000
            THEN 'medium'
       ELSE 'small' END
       AS geosize_group
INTO countries_plus
FROM countries;
```
You will now explore the relationship between the size of a country in terms of surface area and in terms of population using grouping fields created with `CASE`.

INSTRUCTIONS 1.1

<img width="442" alt="image" src="https://user-images.githubusercontent.com/68601128/120253537-00bc8000-c25e-11eb-8fed-afd0bd4823e6.png">

```SQL
SELECT country_code, size,
    -- 1. First case
    CASE WHEN size > 50000000 THEN 'large'
        -- 2. Second case
        WHEN size > 1000000 THEN 'medium'
        -- 3. Else clause + end
        ELSE 'small' END
        -- 4. Alias name (popsize_group)
        AS popsize_group
-- 5. From table
FROM populations
-- 6. Focus on 2015
WHERE year = 2015;
```

OUTPUT

<img width="747" alt="image" src="https://user-images.githubusercontent.com/68601128/120253567-15007d00-c25e-11eb-9e8c-e360a86c7cc3.png">

INSTRUCTION 1.2

+ Use `INTO` to save the result of the previous query as `pop_plus`. You can see an example of this in the countries_plus code in the assignment text. Make sure to include a `; ` at the end of your `WHERE` clause!

+ Then, include another query below your first query to display all the records in pop_plus using `SELECT * FROM pop_plus`; so that you generate results and this will display `pop_plus` in query result.

```SQL
SELECT country_code, size,
    CASE WHEN size > 50000000 THEN 'large'
        WHEN size > 1000000 THEN 'medium'
        ELSE 'small' END
        AS popsize_group
-- 1. Into table
INTO pop_plus
FROM populations
WHERE year = 2015;

-- 2. Select all columns of pop_plus
SELECT * FROM pop_plus
```
output

<img width="747" alt="image" src="https://user-images.githubusercontent.com/68601128/120253993-2eee8f80-c25f-11eb-9b16-180555d2adb4.png">

INSTRUCTION 1.3

+ Keep the first query intact that creates pop_plus using `INTO`.
+ Write a query to join `countries_plus AS c` on the left with `pop_plus AS p` on the right matching on the country code fields.
+ Sort the data based on geosize_group, in ascending order so that large appears on top.
+ Select the `name`, `continent`, `geosize_group`, and `popsize_group` fields.

### CHAPTER 2 - OUTER JOINs

**LEFT and RIGHT JOINs

Congratulations on completing Chapter 1 on INNER JOINs. Welcome to Chapter 2 on OUTER JOINs! You can remember outer joins as reaching OUT to another table while keeping all of the records of the original table. Inner joins keep only the records IN both tables. You'll begin this chapter by exploring (1) LEFT JOINs, (2) RIGHT JOINs, and (3) FULL JOINs, which are the three types of OUTER JOINs. Let's begin by exploring how a LEFT JOIN differs from an INNER JOIN via a diagram. 

<img width="318" alt="image" src="https://user-images.githubusercontent.com/68601128/120348138-46676000-c2d3-11eb-97e2-f5b9d165f100.png">


<img width="894" alt="image" src="https://user-images.githubusercontent.com/68601128/120255722-010b4a00-c263-11eb-9c67-3b4352eea4f2.png">

<img width="590" alt="image" src="https://user-images.githubusercontent.com/68601128/120349306-62b7cc80-c2d4-11eb-8e9b-dd2f34f83ecc.png">

The RIGHT JOIN is much less common than the LEFT JOIN so we won't spend as much time on it here. 

<img width="638" alt="image" src="https://user-images.githubusercontent.com/68601128/120363636-bf21e880-c2e2-11eb-9b59-f9e80856184b.png">

**LEFT JOIN EXAMPLES**

Now you'll explore the differences between performing an inner join and a left join using the cities and countries tables.

You'll begin by performing an inner join with the cities table on the left and the countries table on the right. Remember to alias the name of the city field as city and the name of the country field as country.

INSTRUCTIONS 1.1 

+ Fill in the code based on the instructions in the code comments to complete the inner join. Note how many records are in the result of the join in the query result tab.

```SQL
-- Select the city name (with alias), the country code,
-- the country name (with alias), the region,
-- and the city proper population
SELECT c1.name AS country, code, c2.name AS city,
       region, city_proper_pop
-- From left table (with alias)
FROM countries AS c1
  -- Join to right table (with alias)
  INNER JOIN cities AS c2
    -- Match on country code
    ON c1.code = c2.country_code
-- Order by descending country code
ORDER BY code DESC;

```
<img width="744" alt="image" src="https://user-images.githubusercontent.com/68601128/120364382-92220580-c2e3-11eb-8321-4f4f3a7b3b23.png">

INSTRUCTION 1.2

+ Change the code to perform a LEFT JOIN instead of an INNER JOIN. After executing this query, note how many records the query result contains.

```SQL
SELECT c1.name AS city, code, c2.name AS country,
       region, city_proper_pop
FROM cities AS c1
  -- 1. Join right table (with alias)
  LEFT JOIN countries AS c2
    -- 2. Match on country code
    ON c1.country_code = c2.code
-- 3. Order by descending country code
ORDER BY code DESC;
```

OUTPUT

<img width="748" alt="image" src="https://user-images.githubusercontent.com/68601128/120364980-46239080-c2e4-11eb-8df4-4c99360b722f.png">

<img width="455" alt="image" src="https://user-images.githubusercontent.com/68601128/120365051-5d627e00-c2e4-11eb-8563-c5f54dc61851.png">


INSTRUCTION

+ Modify your code to calculate the average GDP per capita AS avg_gdp for each region in 2010.
+ Select the region and avg_gdp fields.

```SQL
-- Select fields
SELECT region, AVG(gdp_percapita) AS avg_gdp
-- From countries (alias as c)
FROM countries AS c
  -- Left join with economies (alias as e)
  LEFT JOIN economies AS e
    -- Match on code field'''
    ON c.code = e.code
-- Focus on 2010
WHERE year = 2010
-- Group by region
GROUP BY region;
```

<img width="749" alt="image" src="https://user-images.githubusercontent.com/68601128/120409826-2a41de00-c328-11eb-9e51-73382d06d647.png">

INSTRUCTION 1.2

+ Arrange this data on average GDP per capita for each region in 2010 from highest to lowest average GDP per capita.

```SQL
-- Select fields
SELECT region, AVG(gdp_percapita) AS avg_gdp
-- From countries (alias as c)
FROM countries AS c
  -- Left join with economies (alias as e)
  LEFT JOIN economies AS e
    -- Match on code fields
    ON c.code = e.code
-- Focus on 2010
WHERE year = 2010
-- Group by region
GROUP BY region
-- Order by descending avg_gdp
ORDER BY avg_gdp DESC;
```

<img width="757" alt="image" src="https://user-images.githubusercontent.com/68601128/120410068-ae946100-c328-11eb-9d72-ccd9b8972dc5.png">

**RIGHT JOINS**

2. INNER JOIN vs LEFT JOIN

Recall that an INNER JOIN keeps only the records that have matching key field values in both tables. A LEFT JOIN keeps all of the records in the left table while bringing in missing values for those key field values that don't appear in the right table.

<img width="614" alt="image" src="https://user-images.githubusercontent.com/68601128/120410372-3c704c00-c329-11eb-8817-d23eda1cced5.png">

3. LEFT JOIN vs RIGHT JOIN

Now you can see the differences between a LEFT JOIN and a RIGHT JOIN. The id values of 2 and 3 in the left table do not match with the id values in the right table, so missing values are brought in for them in the LEFT JOIN. Likewise for the RIGHT JOIN, missing values are brought in for id values of 5 and 6. 

<img width="611" alt="image" src="https://user-images.githubusercontent.com/68601128/120410476-72adcb80-c329-11eb-80a9-d8c51bce8ad8.png">

5. FULL JOIN diagram

Note the missing values here and that all six of the values of id are included in the table. You can also see from the SQL code to produce this FULL JOIN result that the general format aligns closely with the SQL syntax you've seen for both an INNER JOIN and a LEFT JOIN. You'll next explore an example from the leaders database. 

<img width="881" alt="image" src="https://user-images.githubusercontent.com/68601128/120410559-96711180-c329-11eb-8706-45b8271bed33.png">

<img width="633" alt="image" src="https://user-images.githubusercontent.com/68601128/120410719-e8199c00-c329-11eb-88fd-03719c68e3b8.png">

<img width="703" alt="image" src="https://user-images.githubusercontent.com/68601128/120410793-14351d00-c32a-11eb-9c30-6660df1e7726.png">

<img width="644" alt="image" src="https://user-images.githubusercontent.com/68601128/120410820-20b97580-c32a-11eb-9dda-25a3b609e6c4.png">

**FULL JOIN EXAMPLES**

In this exercise, you'll examine how your results differ when using a full join versus using a left join versus using an inner join with the `countries` and `currencies` tables.

You will focus on the North American `region` and also where the `name` of the country is missing. Dig in to see what we mean!

Begin with a full join with countries on the left and currencies on the right. The fields of interest have been SELECTed for you throughout this exercise.

Then complete a similar left join and conclude with an inner join.

`Countries table`

<img width="1094" alt="image" src="https://user-images.githubusercontent.com/68601128/120410995-6f670f80-c32a-11eb-827b-4feeecf336c6.png">

`Currencies table`

<img width="1090" alt="image" src="https://user-images.githubusercontent.com/68601128/120411041-80b01c00-c32a-11eb-9a70-97b7809640ae.png">

INSTRUCTIONS 1.1

+ Choose records in which `region` corresponds to North America or is `NULL`.

```SQL
SELECT name AS country, code, region, basic_unit
-- 3. From countries
FROM countries
  -- 4. Join to currencies
  FULL JOIN currencies
    -- 5. Match on code
    USING (code) -- É usado quando os nomes da coluna são iguais, como todos são code, então para facilitar uso USING code e não countries.code = currencies.code
-- 1. Where region is North America or null
WHERE region = 'North America' OR region IS null 
-- 2. Order by region
ORDER BY region;
```

INSTRUCTIONS 1.2

+ Repeat the same query as above but use a LEFT JOIN instead of a FULL JOIN. Note what has changed compared to the FULL JOIN result!

```SQL 

SELECT name AS country, code, region, basic_unit
-- 1. From countries
FROM countries
  -- 2. Join to currencies
  LEFT JOIN currencies
    -- 3. Match on code
    USING (code)
-- 4. Where region is North America or null
WHERE region = 'North America' OR region IS null
-- 5. Order by region
ORDER BY region;
```

<img width="765" alt="image" src="https://user-images.githubusercontent.com/68601128/120411677-940fb700-c32b-11eb-83e8-6d5a613b0bd9.png">

INSTRUCTIONS 1.3

+ Repeat the same query as above but use an `INNER JOIN` instead of a `FULL JOIN`. Note what has changed compared to the FULL JOIN and LEFT JOIN results!

```SQL
SELECT name AS country, code, region, basic_unit
FROM countries
  -- 1. Join to currencies
  INNER JOIN currencies
    USING (code)
-- 2. Where region is North America or null
WHERE region = 'North America' OR region IS NULL
-- 3. Order by region
ORDER BY region;
```
<img width="775" alt="image" src="https://user-images.githubusercontent.com/68601128/120411813-d33e0800-c32b-11eb-871f-0e36863a362b.png">

Have you kept an eye out on the different numbers of records these queries returned? The FULL JOIN query returned 17 rows, the OUTER JOIN returned 4 rows, and the INNER JOIN only returned 3 rows. Do these results make sense to you?

**FULL JOIN EXAMPLES (2)**

You'll now investigate a similar exercise to the last one, but this time focused on using a table with more records on the left than the right. You'll work with the languages and countries tables.

countries table

<img width="825" alt="image" src="https://user-images.githubusercontent.com/68601128/120412293-b1915080-c32c-11eb-8cb4-8546cd1839fe.png">

languages table

<img width="831" alt="image" src="https://user-images.githubusercontent.com/68601128/120412327-c1a93000-c32c-11eb-90fa-d1c95b9a32e9.png">



Begin with a full join with languages on the left and countries on the right. Appropriate fields have been selected for you again here.


INSTRUCTION 1.1

+ Choose records in which countries.name starts with the capital letter 'V' or is NULL.
+ Arrange by countries.name in ascending order to more clearly see the results.


```sql
SELECT countries.name, code, languages.name AS language
-- 3. From languages
FROM languages
  -- 4. Join to countries
   FULL JOIN countries
    -- 5. Match on code
    USING (code)
-- 1. Where countries.name starts with V or is null
WHERE countries.name LIKE 'V%' OR countries.name IS NULL
-- 2. Order by ascending countries.name
ORDER BY countries.name;
```
<img width="829" alt="image" src="https://user-images.githubusercontent.com/68601128/120412391-dbe30e00-c32c-11eb-89fa-0d3c0370e6a1.png">

INSTRUCTION 1.2

+ Repeat the same query as above but use a left join instead of a full join. Note what has changed compared to the full join result!

```SQL

SELECT countries.name, code, languages.name AS language
FROM languages
  -- 1. Join to countries
  LEFT JOIN countries
    -- 2. Match using code
    USING (code)
-- 3. Where countries.name starts with V or is null
WHERE countries.name LIKE 'V%' OR countries.name IS NULL
ORDER BY countries.name;
```

<img width="818" alt="image" src="https://user-images.githubusercontent.com/68601128/120412563-249ac700-c32d-11eb-91c1-9f972bd54758.png">

INSTRUCTIONS 1.3

+ Repeat once more, but use an inner join instead of a left join. Note what has changed compared to the full join and left join results.

```SQL
SELECT countries.name, code, languages.name AS language
FROM languages
  -- 1. Join to countries
  INNER JOIN countries
    USING (code)
-- 2. Where countries.name starts with V or is null
WHERE countries.name LIKE 'V%' OR countries.name IS NULL
ORDER BY countries.name;
```

<img width="838" alt="image" src="https://user-images.githubusercontent.com/68601128/120412683-5ad84680-c32d-11eb-855e-552104646186.png">

Well done. Again, make sure to compare the number of records the different types of joins return and try to verify whether the results make sense.

**FULL JOIN (3)**

You'll now explore using two consecutive full joins on the three tables you worked with in the previous two exercises.

INSTRUCTIONS

+ Complete a full join with countries on the left and languages on the right.
+ Next, full join this result with currencies on the right.
+ Use LIKE to choose the Melanesia and Micronesia regions (Hint: 'M%esia').
+ Select the fields corresponding to the country name AS country, region, language name AS language, and basic and fractional units of currency.

```sql
-- 7. Select fields (with aliases)
SELECT c1.name AS country, region, l.name AS language, basic_unit, frac_unit
-- 1. From countries (alias as c1)
FROM countries AS c1
  -- 2. Join with languages (alias as l)
  FULL JOIN languages AS l
    -- 3. Match on code
    USING (code)
  -- 4. Join with currencies (alias as c2)
  FULL JOIN currencies AS c2
    -- 5. Match on code
    USING (code)
-- 6. Where region like Melanesia and Micronesia
WHERE region LIKE 'M%esia';
```

<img width="747" alt="image" src="https://user-images.githubusercontent.com/68601128/120413317-6b3cf100-c32e-11eb-9aee-c2be22e1a0f2.png">


**CROSS JOIN**

2. CROSS JOIN diagram

In this diagram we have two tables named table1 and table2. Each table only has one field, both with the name of id. The result of the CROSS JOIN is all nine combinations of the id values of 1, 2, and 3 in table1 with the id values of A, B, and C for table2. Next you'll explore an example from the leaders database and look over the SQL syntax for a CROSS JOIN. 

<img width="159" alt="image" src="https://user-images.githubusercontent.com/68601128/120413433-aa6b4200-c32e-11eb-8353-1c08cd83639e.png">

3. Pairing prime ministers with presidents

Suppose that all prime ministers in North America and Oceania in the prime_ministers table are scheduled for individual meetings with all presidents in the presidents table. You can look at all of these combinations by using a CROSS JOIN. The syntax here remains similar to what you've seen earlier in the course. We use a WHERE clause to focus on only prime ministers in North America and Oceania in the prime_ministers table. The results of the query give us the pairings for the two prime ministers in North America and Oceania from the prime_ministers table with the seven presidents in the presidents table. 

<img width="609" alt="image" src="https://user-images.githubusercontent.com/68601128/120413579-f0c0a100-c32e-11eb-89db-5c6d195a202f.png">

A table of two cities

This exercise looks to explore languages potentially and most frequently spoken in the cities of Hyderabad, India and Hyderabad, Pakistan.

You will begin with a cross join with cities AS c on the left and languages AS l on the right. Then you will modify the query using an inner join in the next tab.

INSTRUCTIONS 1.1

+ Create the cross join as described above. (Recall that cross joins do not use ON or USING.)
+ Make use of LIKE and Hyder% to choose Hyderabad in both countries.
+ Select only the city name AS city and language name AS language.

```sql
-- 4. Select fields
SELECT c.name AS city, l.name AS language
-- 1. From cities (alias as c)
FROM cities AS c        
  -- 2. Join to languages (alias as l)
  CROSS JOIN languages AS l 
-- 3. Where c.name like Hyderabad
WHERE c.name LIKE 'Hyder%';
```

<img width="750" alt="image" src="https://user-images.githubusercontent.com/68601128/120413902-7d6b5f00-c32f-11eb-9b9f-52638cd914d6.png">

INSTRUCTIONS 1.2

+ use an inner join instead of a cross join. Think about what the difference will be in the results for this inner join result and the one for the cross join.

```SQL
-- 5. Select fields
SELECT c.name AS city, l.name AS language 
-- 1. From cities (alias as c)
FROM cities AS c     
  -- 2. Join to languages (alias as l)
  INNER JOIN languages AS l
    -- 3. Match on country code
    ON c.country_code = l.code
-- 4. Where c.name like Hyderabad
WHERE c.name LIKE 'Hyder%';
```
<img width="747" alt="image" src="https://user-images.githubusercontent.com/68601128/120414330-303bbd00-c330-11eb-9c8c-a2551ea62f23.png">

Good one! Can you see the difference between a CROSS JOIN and a INNER JOIN?

**Outer challenge**

Now that you're fully equipped to use outer joins, try a challenge problem to test your knowledge!

In terms of life expectancy for 2010, determine the names of the lowest five countries and their regions.

INSTRUCTIONS

+ Select country name AS country, region, and life expectancy AS life_exp.
+ Make sure to use LEFT JOIN, WHERE, ORDER BY, and LIMIT.

```SQL
-- Select fields
SELECT c.name AS country, region,
life_expectancy AS life_exp
-- From countries (alias as c)
FROM countries AS c
  -- Join to populations (alias as p)
  LEFT JOIN populations AS p
    -- Match on country code
    ON c.code = p.country_code
-- Focus on 2010
WHERE year = 2010
-- Order by life_exp
ORDER BY life_exp
-- Limit to 5 records
LIMIT 5; 
```

<img width="751" alt="image" src="https://user-images.githubusercontent.com/68601128/120414822-ef907380-c330-11eb-99bb-a4dc81f2a0de.png">


**STATE OF THE UNION**

<img width="909" alt="image" src="https://user-images.githubusercontent.com/68601128/120532264-e3022e80-c3b5-11eb-8901-57a9afa2d53a.png">

<img width="238" alt="image" src="https://user-images.githubusercontent.com/68601128/120532383-0200c080-c3b6-11eb-86b3-e1c5104b7dbf.png">

<img width="206" alt="image" src="https://user-images.githubusercontent.com/68601128/120532475-1644bd80-c3b6-11eb-9c85-0490a9e7c8c6.png">

By contrast (with the same two tables left_one and right_one), UNION ALL includes all duplicates in its result. So left_one and right_one both having four records yields eight records for the result of the UNION ALL. If it were the case that right_one had these same four values and also one more value of 1 for id, you'd see three entries for 1 in the resulting UNION ALL. Let's check out the SQL syntax using the leaders database for both UNION and UNION ALL, but first you'll see one more table in the leaders database. 

<img width="603" alt="image" src="https://user-images.githubusercontent.com/68601128/120532581-2e1c4180-c3b6-11eb-9ded-7815d1cfe74d.png">

<img width="605" alt="image" src="https://user-images.githubusercontent.com/68601128/120532649-455b2f00-c3b6-11eb-88ec-75ff113b6d1b.png">

that UNION and UNION ALL clauses do not do the lookup step that JOINs do. They simply stack records on top of each other from one table to the next. 

**UNION EXAMPLES**

Economies table

<img width="1221" alt="image" src="https://user-images.githubusercontent.com/68601128/120533496-26a96800-c3b7-11eb-8110-75d8b170972d.png">

Economies2015 table

<img width="1218" alt="image" src="https://user-images.githubusercontent.com/68601128/120533527-3163fd00-c3b7-11eb-87b5-2ab83843c6bc.png">

Economies2010 table

<img width="1221" alt="image" src="https://user-images.githubusercontent.com/68601128/120533587-42ad0980-c3b7-11eb-8f71-83382f4a0fc6.png">


INSTRUCTION

+ Combine these two tables into one table containing all of the fields in economies2010. The economies table is also included for reference.
+ Sort this resulting single table by country code and then by year, both in ascending order.

```SQL
-- Select fields from 2010 table
SELECT *
  -- From 2010 table
FROM economies2010
	-- Set theory clause
UNION
-- Select fields from 2015 table
SELECT *
  -- From 2015 table
FROM economies2015
-- Order by code and year
ORDER BY code, year;
```

<img width="757" alt="image" src="https://user-images.githubusercontent.com/68601128/120533410-15f8f200-c3b7-11eb-8eec-ee8658d5ddc3.png">


**UNION 2 EXAMPLE**

INSTRUCTION 

+ Determine all (non-duplicated) country codes in either the cities or the currencies table. The result should be a table with only one field called country_code.
+ Sort by country_code in alphabetical order.

```SQL 
-- Select field
SELECT DISTINCT country_code
  -- From cities
  FROM cities
	-- Set theory clause
	UNION
-- Select field
SELECT DISTINCT code
  -- From currencies
  FROM currencies
-- Order by country_code
order by country_code;
```

<img width="517" alt="image" src="https://user-images.githubusercontent.com/68601128/120534023-c0711500-c3b7-11eb-94b1-d2b5bca9071a.png">

**UNION ALL EXAMPLE**

As you saw, duplicates were removed from the previous two exercises by using `UNION`.

To include duplicates, you can use `UNION ALL`.

INSTRUCTION

+ Determine all combinations (include duplicates) of country code and year that exist in either the economies or the populations tables. Order by code then year.
+ The result of the query should only have two columns/fields. Think about how many records this query should result in.
+ You'll use code very similar to this in your next exercise after the video. Make note of this code after completing it.

```SQL
-- Select fields
SELECT code, year
  -- From economies
  FROM economies
	-- Set theory clause
	UNION ALL
-- Select fields
SELECT country_code, year
  -- From populations
  FROM populations
-- Order by code, year
ORDER BY code, year;
```

<img width="749" alt="image" src="https://user-images.githubusercontent.com/68601128/120534438-35444f00-c3b8-11eb-929b-1ba07a2d7abd.png">


**INTERSECT DIAGRAM AND SQL CODE**

Vale lembrar que intersect precisa ter o SELECT igual na coluna.

<img width="646" alt="image" src="https://user-images.githubusercontent.com/68601128/120534662-7ccadb00-c3b8-11eb-9bac-ad3ef10cc98c.png">


<img width="622" alt="image" src="https://user-images.githubusercontent.com/68601128/120534743-92d89b80-c3b8-11eb-990f-2b80897d0435.png">

Next, let's think about what would happen if we tried to select two columns instead of one from our previous example. The code shown does just that. What will be the result of this query? Will this also give you the names of the countries that have both a prime minister and a president? Hmmm [PAUSE] The actual result is an empty table. Why is that? When INTERSECT looks at two columns it includes both columns in the search. So it didn't find any countries with prime ministers AND presidents having the same name. INTERSECT looks for RECORDS in common, not individual key fields like what a join does to match. This is an important distinction.

<img width="596" alt="image" src="https://user-images.githubusercontent.com/68601128/120534861-b4398780-c3b8-11eb-9ac0-f3e85de5261a.png">

**INTERSECT EXAMPLE**

+ Again, order by `code` and then by `year`, both in ascending order.
+ Note the number of records here (given at the bottom of query result) compared to the similar `UNION ALL` query result (814 records).

```SQL
-- Select fields
SELECT code, year
  -- From economies
  FROM economies
	-- Set theory clause
	INTERSECT
-- Select fields
SELECT country_code, year
  -- From populations
  FROM populations
-- Order by code and year
ORDER BY code, year;
```

<img width="718" alt="image" src="https://user-images.githubusercontent.com/68601128/120535480-65d8b880-c3b9-11eb-9315-845a231073cd.png">


**INTERSCT 2 EXAMPLE**

As you think about major world cities and their corresponding country, you may ask which countries also have a city with the same name as their country name?

INSTRUCTIONS

Use `INTERSECT` to answer this question with countries and cities!

```SQL 
-- Select fields
SELECT name, code
  -- From countries
  FROM countries
	-- Set theory clause
	INTERSECT
-- Select fields
SELECT name, country_code
  -- From cities
FROM cities;
```
<img width="708" alt="image" src="https://user-images.githubusercontent.com/68601128/120536168-370f1200-c3ba-11eb-9ba6-2fe77e59c0a0.png">

**EXCEPTIONAL**

<img width="601" alt="image" src="https://user-images.githubusercontent.com/68601128/120543205-70e41680-c3c2-11eb-84db-7623cc43d471.png">







