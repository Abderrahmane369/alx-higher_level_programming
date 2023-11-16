-- TASK 9
-- LETS GO
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON states.id = cities.state_id;

