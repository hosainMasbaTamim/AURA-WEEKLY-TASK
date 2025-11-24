-- this is the code for the db running on the xamppp server

CREATE DATABASE todo_cli;

USE todo_cli;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task VARCHAR(255) NOT NULL,
    done TINYINT(1) DEFAULT 0
);
