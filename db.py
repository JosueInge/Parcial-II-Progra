import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="tu_usuario",      
        password="tu_password",
        database="db_academica"
    )

def insert_user(usuario, clave, nombre, direccion, telefono):
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO usuarios (usuario, clave, nombre, direccion, telefono) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (usuario, clave, nombre, direccion, telefono))
    db.commit()
    cursor.close()
    db.close()

def get_all_users():
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    users = cursor.fetchall()
    cursor.close()
    db.close()
    return users

def delete_user(idUsuario):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM usuarios WHERE idUsuario = %s", (idUsuario,))
    db.commit()
    cursor.close()
    db.close()

def update_user(idUsuario, usuario, clave, nombre, direccion, telefono):
    db = connect_db()
    cursor = db.cursor()
    query = """UPDATE usuarios SET usuario = %s, clave = %s, nombre = %s, direccion = %s, telefono = %s
               WHERE idUsuario = %s"""
    cursor.execute(query, (usuario, clave, nombre, direccion, telefono, idUsuario))
    db.commit()
    cursor.close()
    db.close()

def verify_login(usuario, clave):
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE usuario = %s AND clave = %s", (usuario, clave))
    user = cursor.fetchone()
    cursor.close()
    db.close()
    return user