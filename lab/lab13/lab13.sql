.read data.sql


CREATE TABLE average_prices AS
  SELECT category, avg(MSRP) AS average_price 
  FROM products
  GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT *
  FROM inventory
  GROUP BY item
  HAVING price = MIN(price) ;


CREATE TABLE shopping_list AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


CREATE TABLE total_bandwidth AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

