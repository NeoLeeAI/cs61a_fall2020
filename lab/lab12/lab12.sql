.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet 
  FROM students
  WHERE pet = 'dog' AND color = 'blue';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song
  FROM students
  WHERE pet = 'dog' AND color = 'blue';


CREATE TABLE smallest_int AS
  SELECT time, smallest
  FROM students
  WHERE smallest > 2
  ORDER BY smallest
  LIMIT 20;


CREATE TABLE matchmaker AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


CREATE TABLE sevens AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

