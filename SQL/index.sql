-- quickly find rows with specific column values
-- Without an index, SQL scans the whole table to locate the relevant rows
CREATE TABLE viewcandidate1(
	id INT NOT NULL UNIQUE,
    name VARCHAR(50) NOT NULL,
    percentage INT NOT NULL ,
    gender VARCHAR(1) NOT NULL,
    branch VARCHAR(10) NOT NULL,
    INDEX(gender(1)),
    UNIQUE KEY unique_name (name)
);

-- INDEXING-> an index is a data structure such as B-Tree that stores the key values for faster lookups.
-- index offers an efficient way to quickly access the records from the database files stored on the disk drive
-- disadv -> index occupies its own space, so indexed data will consume more disk space too
CREATE INDEX candidateindex ON viewcandidate(percentage);
SELECT name, percentage FROM viewcandidate WHERE percentage > 35;
SHOW INDEX FROM viewcandidate1;
DROP INDEX candidateindex ON viewcandidate;

-- composite indexes -> index on multiple columns
CREATE TABLE viewcandidate2(
	id INT NOT NULL UNIQUE,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    INDEX person(name, age)
);

EXPLAIN SELECT * FROM viewcandidate2;

-- A cluster index is the table itself, which enforces the order of the rows in the table.
-- An innoDB table always has a clustered index.
-- It is an index that enforces the ordering on the rows of the table physically.
-- clustered index store the rows in sorted order, each table have only one clustered index
-- each InnoDB table always has one and only one clustered index
-- All indexes other than the clustered index are the non-clustered indexes or secondary indexes


-- Index cardinality refers to the uniqueness of values stored in a specified column within an index
-- to generate an optimal query plan for a given query

CREATE TABLE IF NOT EXISTS contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL,
    UNIQUE KEY unique_email (email)
);

SHOW INDEXES FROM contacts;

INSERT INTO contacts(first_name,last_name,phone,email)
VALUES('ABC','EFG','987451230','c@gmail.com');

CREATE UNIQUE INDEX idx_name_phone
ON contacts(first_name,last_name,phone);

 -- MySQL considers NULL values as distinct values. Therefore, you can have multiple NULL values in the UNIQUE index
 -- UNIQUE constraint does not apply to NULL values
 
 -- PREFIX INDEX to create indexes for string columns.
 -- In case the columns are the string columns, the index will consume a lot of disk space and slow down the INSERT operations.
-- To address this issue, MySQL allows to create an index for the leading part of the column values of the string columns
CREATE TABLE bikeproducts (
  productCode int NOT NULL,
  productName varchar(70) NOT NULL,
  quantityInStock int NOT NULL,
  buyPrice decimal(10,2) NOT NULL,
  MSRP decimal(10,2) NOT NULL,
  PRIMARY KEY (productCode)
);
drop table bikeproducts;
INSERT INTO bikeproducts VALUES ('1','TVS',1000,'48.81','45.10'), ('2','Honda',800,'15.21','12.02'), ('3','Honda city',700,'18.20','20.65');

EXPLAIN SELECT productName,buyPrice,msrp FROM bikeproducts WHERE productName = 'TVS';

SELECT COUNT(DISTINCT LEFT(productName, 6)) unique_rows FROM bikeproducts;

CREATE INDEX idx_productname ON bikeproducts(productName(6));

-- INVISIBLE INDEX -> The invisible indexes allow to mark indexes as unavailable for the query optimizer
CREATE INDEX idx_productname ON bikeproducts(productName(6)) INVISIBLE;

SHOW INDEXES FROM bikeproducts;

SELECT * FROM bikeproducts;

-- table which has no primary key, considers uniqe key on nott null values as primary key and index on the primary key column cannot be invisible
CREATE TABLE bikeproducts1 (
  productCode int NOT NULL,
  productName varchar(70) NOT NULL,
  quantityInStock int NOT NULL,
  buyPrice decimal(10,2) NOT NULL,
  MSRP decimal(10,2) NOT NULL,
  UNIQUE index_msrp(MSRP)
);

ALTER TABLE bikeproducts1
ALTER INDEX index_msrp INVISIBLE; -- Error Code: 3522. A primary key index cannot be invisible   

-- composite index is an index on multiple columns
-- The query optimizer uses the composite indexes for queries that test all columns in the index, or queries that test the first columns, the first two columns, and so on.
CREATE TABLE bikeproducts2 (
  productCode int NOT NULL,
  productName varchar(70) NOT NULL,
  quantityInStock int NOT NULL,
  buyPrice decimal(10,2) NOT NULL,
  MSRP decimal(10,2) NOT NULL,
  PRIMARY KEY (productCode)
);

CREATE INDEX comp_index
ON bikeproducts2(productName, quantityInStock);

SHOW INDEXES FROM bikeproducts2;

-- Index cardinality refers to the uniqueness of values stored in a specified column within an index.
-- query optimizer uses the index cardinality to generate an optimal query plan for a given query. 
-- It also uses the index cardinality to decide whether to use the index or not in the join operations
-- If the query optimizer chooses the index with a low cardinality, it is may be more effective than scan rows without using the index.


-- adding more that one primary key in table
CREATE TABLE Customers (
          order_id INT,
          product_id INT,
          amount INT,
          PRIMARY KEY (order_id, product_id)
          ) ;
     
Describe Customers;

INSERT INTO Customers (order_id, product_id, amount)  
VALUES (101, 509, 800), (102, 610, 799), (103, 702, 650);

SELECT * FROM Customers;

INSERT INTO Customers (order_id, product_id, amount)  
VALUES (103, 702, 699);  -- throws error Error Code: 1062. Duplicate entry '103-702' for key 'customers.PRIMARY'

-- adding more than one unique constraints
CREATE TABLE Customers1 (
		order_id INT NOT NULL auto_increment,
		product_id INT NOT NULL,
		amount INT NOT NULL,
        quantity INT NOT NULL,
		PRIMARY KEY (order_id),
		CONSTRAINT UC1_Customers1 UNIQUE (product_id, amount),
		CONSTRAINT UC2_Customers1 UNIQUE (product_id, quantity)
     );
     
drop table Customers1;
Describe Customers1;
select * from Customers1;
INSERT INTO Customers1 (product_id, amount, quantity)  
VALUES (509, 800, 5), (610, 799, 6), (702, 650, 4);
INSERT INTO Customers1 (product_id, amount, quantity)  
VALUES (702, 651, 4); -- error
INSERT INTO Customers1 (product_id, amount, quantity)  
VALUES (702, 650, 2); -- error