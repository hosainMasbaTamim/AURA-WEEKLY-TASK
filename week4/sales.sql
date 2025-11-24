-- this is the code for the db running on the xamppp server

CREATE DATABASE sales_cli;

USE sales_cli;

CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    sale_date DATE NOT NULL
);
