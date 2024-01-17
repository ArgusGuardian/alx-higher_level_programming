-- list all the cities in the database
USE hbtn_0d_usa;
SELECT cities.id, cities.name, DISTINCT states.name
ORDER BY cities.id;
