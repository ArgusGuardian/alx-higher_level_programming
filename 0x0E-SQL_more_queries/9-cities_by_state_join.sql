-- list all the cities in the database
USE hbtn_0d_usa;
SELECT DISTINCT cities.id, cities.name, states.name
ORDER BY cities.id;
