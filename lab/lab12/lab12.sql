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
  SELECT first.pet as pet, first.song as song, first.color, second.color
  FROM students as first, students as second
  WHERE first.time != second.time AND first.pet = second.pet AND first.song = second.song;
  

CREATE TABLE sevens AS
  SELECT a.seven
  FROM students as a, numbers as b
  WHERE a.time = b.time AND a.number = 7 AND b.'7' = "True";

