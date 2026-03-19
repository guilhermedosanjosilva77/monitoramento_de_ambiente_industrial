
CREATE DATABASE IF NOT EXISTS ambtech;
USE ambtech;

CREATE TABLE IF NOT EXISTS registros (
    id            INT          NOT NULL AUTO_INCREMENT,
    data_hora     DATETIME     NOT NULL,
    temperatura   FLOAT        NOT NULL,
    umidade       FLOAT        NOT NULL,
    data_insercao DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);