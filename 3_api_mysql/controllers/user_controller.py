from db.config import get_connection
from fastapi import HTTPException
from models.user_model import User, UserCreate
import aiomysql

async def lista_usuarios():
    try:
        conn=await get_connection()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("SELECT * FROM upgrade_shop.users")
            data=await cursor.fetchall()
            return data
    except Exception as e:
        raise HTTPException (status_code=500, detail=f"Error : {str(e)}")



async def obtener_usuario(id_user):
    try:
        conn=await get_connection()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("SELECT * FROM upgrade_shop.users WHERE id=%s",(id_user, ))
            data= await cursor.fetchone()
        if data:
            return data
        else:
            raise HTTPException(status_code=404, detail='Usuario no encontrado')
    except Exception as e:
        raise HTTPException (status_code=500, detail=f"Error: {str(e)}")
    finally:
        conn.close()

        

async def actualizar_usuario(id_user:int, user: User):
    if id_user != user.id:
        raise HTTPException(status_code=400, detail='El ID no coincide')
    try:
        conn=await get_connection()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("UPDATE upgrade_shop.users SET name=%s, age=%s, surname=%s, email=%s, status=%s, password=%s, rol=%s WHERE id=%s", (
                user.name,
                user.age,
                user.surname,
                user.email,
                user.status,
                user.password,
                user.rol,
                id_user
            ))
            await conn.commit()
            user = await obtener_usuario(id_user)
            return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
        conn.close()

async def borrar_usuario(id_user):
        try:
            conn=await get_connection()
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                user=await obtener_usuario(id_user)#comprobar si existe el user
                if not user:
                    raise HTTPException(status_code=404, detail=f'Usuario con id {id_user} no encontrado')
                #borrar el usuario
                await cursor.execute("DELETE FROM upgrade_shop.users WHERE id=%s", (id_user, ))
                await conn.commit()
                return{"msg": f'El usuario con id {id_user} ha sido eliminado exitosamente', 'status':True}
        except Exception as e:
            raise HTTPException (status_code=500, detail=f"Error: {str(e)}")
        finally:
            conn.close()