import os
import aiomysql
from dotenv import load_dotenv

load_dotenv()


#copiamos y pegamos
async def get_connection(): 
    return await aiomysql.connect(
        host=os.getenv("MYSQL_HOST"),
        port=int(os.getenv("MYSQL_PORT")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        db=os.getenv("MYSQL_DATABASE")
    )