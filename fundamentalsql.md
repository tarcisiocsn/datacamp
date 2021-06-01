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











