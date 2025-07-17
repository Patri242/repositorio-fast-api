from fastapi import APIRouter
from controllers import auth_controller
from models.user_model import UserCreate, UserLogin

#creamos ruta

router = APIRouter()

#registro de usuarios
@router.post('/register', status_code=201) #201 cuando guardamos info
async def register_user(user:UserCreate):
    return await auth_controller.registrar_usuario(user)

#ruta login usuario
@router.post("/login", status_code=200)
async def login(user_login: UserLogin):
    return await auth_controller.login(user_login)