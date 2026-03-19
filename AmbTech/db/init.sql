USE ambeTech

CREATE TABLE registros(

    id INT NOT NULL AUTO_INCREMENT,

    data_hora  DATE NOT NULL,

    temperatura FLOAT NOT NULL,

    umidade FLOAT NOT NULL,

    data_insercao DATE NOT NULL,

    PRIMARY KEY (id)

)