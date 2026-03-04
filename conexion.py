import os #importa desde la terminal del sistema las varibales permanentes 
import mysql.connector
from mysql.connector import Error

#setx DB_PASS 1234
#Desglose:
#setx:comando para guardar variable permanente
#DB_PASS:nombre de la variable
#1234:valor que se guarda

try:
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),  #llamada de las variables permanentes para la conexion a la base de datos
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME")
    )

    if connection.is_connected():
        print("Conexion establecida")

except Error as ex:
    print(f"Error durante la conexion: {ex}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Conexion a la base de datos cerrada")