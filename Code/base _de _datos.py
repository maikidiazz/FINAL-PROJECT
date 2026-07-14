
import mysql.connector
from mysql.connector import Error


def create_connection():
    """Establece una conexión a la base de datos MySQL."""
    conection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="proyecto_final",
            user="root",
            password=""
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None


create_connection()

conexion = create_connection()
