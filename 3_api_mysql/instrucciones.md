# API con MYSQL.

    1 - Crear un bbdd MySQL llama upgrade-shop: Y crear la siguiente tabla
                products
                    id
                    title
                    price
                    quantity
                    status

    2 - "fastapi[standard]"
        python-dotenv
        mysql-connector-python

    3 - pip list y creais el fichero requirements.txt

## ENTIDAD USUARIOS:
    -crear una tabla users en la BBDD
        -id:int
        -name:str
        -surname:str
        -age:int
        -email:str
        -register_date: date =>default now()
        -status:int ->Boolean
        -password:str
        -rol: ENUM('admin', 'user')

    -crear fichero routes, models y controllers especificos para users
    -models modelo de users sin id y con id
    -routes GET users/id => obtener los datos de un usuario
            PUT users/id => actualizar los datos de un usuario
            DEL users/id => borrar un usuario

        - TODO: CASA HACER LA RUTA PARA OBTENER TODOS LOS USUARIOS => GETALL
        - TODO: CASA HACER LA RUTA PARA REGISTRAR UN USUARIO. => REGISTER => POST




-Para la chati- quiero que me generes una lista de.. con esta tabla
 CREATE TABLE `upgrade_shop`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(25) NOT NULL,
  `surname` VARCHAR(60) NOT NULL,
  `age` INT NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `register_date` TIMESTAMP NOT NULL DEFAULT now(),
  `status` TINYINT NOT NULL DEFAULT 1,
  `password` VARCHAR(255) NOT NULL,
  `rol` ENUM('admin', 'user') NOT NULL DEFAULT 'user',
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

