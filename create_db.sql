-- prepare the mysql server for the project

CREATE DATABASE IF NOT EXISTS developerHome_db;
CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'Pass_123';
GRANT ALL PRIVILEGES ON `developerHome_db`.* TO 'admin'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;
