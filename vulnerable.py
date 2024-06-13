import sqlite3
import os

# Conexión a la base de datos (puede ser cualquier base de datos SQLite)
def conectar_db():
    conn = sqlite3.connect('vulnerable.db')
    return conn

# Función con vulnerabilidad de inyección SQL
def obtener_usuario(username):
    conn = conectar_db()
    cursor = conn.cursor()
    # Vulnerabilidad de inyección SQL
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

# Función con vulnerabilidad de inyección de comandos del sistema operativo
def listar_archivos(directorio):
    # Vulnerabilidad de inyección de comandos
    comando = f"ls {directorio}"
    os.system(comando)

# Función con uso de función insegura (eval)
def evaluar_expresion(expresion):
    # Uso inseguro de eval
    return eval(expresion)

# Función principal para probar las vulnerabilidades
def main():
    username = input("Introduce el nombre de usuario: ")
    print("Obteniendo usuario...")
    print(obtener_usuario(username))

    directorio = input("Introduce el directorio a listar: ")
    print("Listando archivos...")
    listar_archivos(directorio)

    expresion = input("Introduce una expresión a evaluar: ")
    print("Evaluando expresión...")
    print(evaluar_expresion(expresion))

if __name__ == "__main__":
    main()
