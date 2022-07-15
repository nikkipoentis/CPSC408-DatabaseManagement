CREATE DATABASE IF NOT EXISTS cpsc408;
USE cpsc408; -- specifies database

CREATE TABLE agency (
agencyID INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
Name VARCHAR(50),
Origin VARCHAR(20)
);

CREATE TABLE astronaut (
astronautID INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
Name VARCHAR(50),
Age INTEGER,
Agency INTEGER NOT NULL,
CONSTRAINT FK_astronaut_agency FOREIGN KEY (Agency) REFERENCES agency(agencyID)
);

CREATE TABLE expedition(
expeditionNumber INTEGER NOT NULL PRIMARY KEY,
Duration INTEGER
);

CREATE TABLE astro_expedition(
ID INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
Expedition INTEGER NOT NULL,
Astronaut INTEGER NOT NULL,
CONSTRAINT FK_astro_expedition_exp FOREIGN KEY (Expedition) REFERENCES expedition(expeditionNumber),
CONSTRAINT FK_astro_expedition_astro FOREIGN KEY (Astronaut) REFERENCES astronaut(astronautID)
);

-- CREATE TABLE staging(
-- Expedition INTEGER NOT NULL,
-- Astronaut VARCHAR(50) NOT NULL,
-- Age INTEGER NOT NULL,
-- Gender VARCHAR(6) NOT NULL,
-- Nationality VARCHAR(20) NOT NULL,
-- Duration INTEGER NOT NULL,
-- Agency VARCHAR(15) NOT NULL,
-- agencyOrigin VARCHAR(20) NOT NULL,
-- CHECK(Age > 0)
-- );
