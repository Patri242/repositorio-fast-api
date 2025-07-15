app/ <!-- featured arquitecture -->
├── controllers/
│   └── user_controller.py
├── models/
│   └── user_model.py <!-- creamos data aqui -->
├── routes/
│   └── user_routes.py
<!--                                                                             ├── data/
                                                                            │   └── users.json  ← array persistido -->
└── main.py


CODIGO DE ERROR DEL SERVIDOR

Operación ========>    Código recomendado
GET    200 ========> OK
POST creado    201 ========> Created
PUT actualizado    200 ========> OK o 204 No Content
DELETE exitoso    200 ========> OK o 204 No Content
Error de validación ========>    400 Bad Request
Recurso no existe ========>    404 Not Found