# EN ESTA PARTE DEL CODIGO SE REALIZARA LA IMPLEMENTACION DE LAS FUNCIONES DE LA APLICACION,
# TANTO BASE DE DATOS COMO LA FUNCIONALIDAD DEL PROGRAMA.


# Esta funcion obtiene el ancho de la terminal para centrar el texto en la pantalla.
import sys
import shutil
import os  # Esta funcion permite limpiar la pantalla de la terminal.
import mysql.connector
from mysql.connector import Error

VERDE = "\033[92m"
ROJO = "\033[91m"
AMARILLO = "\033[93m"
RESET = "\033[0m"

usuario = "admin"
constrasena = "admin"


def conectar():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="proyecto_final",
            user="root",
            password=""
        )
        return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


# Esta funcion centra el texto en la pantalla, para que se vea mas estetico y profesional.
def centrar_texto(texto):
    ancho = shutil.get_terminal_size().columns
    lineas = texto.split("\n")
    lineas_centradas = [linea.center(ancho) for linea in lineas]
    return "\n".join(lineas_centradas)


def mostrar_logo_siga():
    logo = r"""
 ____ ___ ____    _
/ ___|_ _/ ___|  / \
\___ \| | |  _  / _ \
 ___) | | |_| |/ ___ \
|____/___\____/_/   \_\

      Sistema Integral de Gestion de Autobuses
---------------------------------------------
      Universidad Tecnologica de Durango
"""
    print(VERDE + centrar_texto(logo) + RESET)


# EN ESTE APARTADO DEL CODIGO SE REALIZARA LA CONEXION A LA BASE DE DATOS, PARA PODER REALIZAR LAS
# OPERACIONES DE LA APLICACION COMO ADMINISTRADOR PARA:
# CREAR, LEER, ACTUALIZAR REGISTROS DE AUTOBUSES, RUTAS, HORARIOS.

def elegir_modo():
    while True:
        limpiar_pantalla()
        mostrar_logo_siga()
        print(AMARILLO + centrar_texto("¿Como quiere ingresar al sistema?") + RESET)
        print(AMARILLO + centrar_texto("1. Modo Administrador") + RESET)
        print(AMARILLO + centrar_texto("2. Modo Usuario") + RESET)
        print(AMARILLO + centrar_texto("3. Salir") + RESET)

        opcion = input(
            AMARILLO + centrar_texto("Ingrese el numero de la opcion: ") + RESET)

        if opcion == "1":
            if login():
                return "admin"
        elif opcion == "2":
            login_usuario()
        elif opcion == "3":
            print(VERDE + centrar_texto("Nos vemos") + RESET)
            input("Presiona Enter para continuar...")
            sys.exit()
        else:
            print(ROJO + centrar_texto("Opción inválida.") + RESET)
            input("Presiona Enter para continuar...")

# Menu de usuario


def menu_usuario():
    while True:
        limpiar_pantalla()
        mostrar_logo_siga()
        print(AMARILLO + centrar_texto("¿Como quiere ingresar al sistema?") + RESET)
        print(AMARILLO + centrar_texto("1. Modo camiones") + RESET)
        print(AMARILLO + centrar_texto("2. Modo Usuario") + RESET)
        print(AMARILLO + centrar_texto("3. Salir") + RESET)

        opcion = input(
            AMARILLO + centrar_texto("Ingrese el numero de la opcion: ") + RESET)

        if opcion == "1":
            if login():
                return "admin"
        elif opcion == "2":
            login_usuario()
        elif opcion == "3":
            print(VERDE + centrar_texto("Nos vemos") + RESET)
            input("Presiona Enter para continuar...")
            break
        else:
            print(ROJO + centrar_texto("Opción inválida.") + RESET)
            input("Presiona Enter para continuar...")

# LOGIN DE ADMINISTRADOR


def login():
    limpiar_pantalla()
    mostrar_logo_siga()
    print(AMARILLO + centrar_texto("Bienvenido al sistema de autobuses") + RESET)

    while True:
        usuario = input(
            AMARILLO + centrar_texto("Ingrese su usuario: ") + RESET)
        contrasena = input(
            AMARILLO + centrar_texto("Ingrese su contraseña: ") + RESET)

        if usuario == "admin" and contrasena == "admin":
            print(VERDE + centrar_texto("Inicio de sesión exitoso") + RESET)
            input("Presiona Enter para continuar...")
            return True
        else:
            print(
                ROJO + centrar_texto("Usuario o contraseña incorrectos. Intente de nuevo.") + RESET)
            input("Presiona Enter para continuar...")


# Login de usuario
def login_usuario():
    while True:
        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)

        limpiar_pantalla()
        mostrar_logo_siga()
        print(AMARILLO + centrar_texto("---MENU USUARIO---") + RESET)

        usuario = input(
            AMARILLO + centrar_texto("Ingrese su usuario: ") + RESET)

        contrasena = input(
            AMARILLO + centrar_texto("Ingrese su contraseña: ") + RESET)

        try:
            cursor.execute(
                "SELECT * FROM usuarios WHERE usuario = %s AND contrasena = %s ", (usuario, contrasena))
            resultado = cursor.fetchone()

            if not resultado:
                print(
                    ROJO + centrar_texto("Usuario o contraseña incorrectos. Intente de nuevo.") + RESET)
                input("Presiona Enter para continuar...")
                cursor.close()
                return elegir_modo()
            else:
                cuenta = resultado
                print(VERDE + centrar_texto("Inicio de sesión exitoso") + RESET)
                input("Presiona Enter para continuar...")
                return menu_usuario()
        except Error as e:
            print("Error de conexion")


if __name__ == "__main__":
    elegir_modo()
