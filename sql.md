# SQL 

## TIPS

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



