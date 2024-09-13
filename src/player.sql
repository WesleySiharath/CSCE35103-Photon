CREATE DATABASE photon_db;

USE photon_db;

CREATE TABLE players 
(
  id INT AUTO_INCREMENT PRIMARY KEY,
  codename VARCHAR(30)
);
INSERT INTO players (id, codename)
VALUES (1, 'Opus');
