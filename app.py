from flask import Flask, render_template, request, redirect, url_for, jsonify
from db import insert_user, get_all_users, delete_user, update_user, verify_login

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def handle_login():
    usuario = request.form['usuario']
    clave = request.form['clave']
    user = verify_login(usuario, clave)
    if user:
        return redirect('/usuarios')
    else:
        return render_template('login.html', error="Usuario o contraseña incorrectos")

@app.route('/usuarios', methods=['GET', 'POST'])
def usuarios():
    if request.method == 'POST':
        usuario = request.form['usuario']
        clave = request.form['clave']
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        insert_user(usuario, clave, nombre, direccion, telefono)
        return redirect(url_for('usuarios'))
    users = get_all_users()
    return render_template('view_users.html', users=users)

@app.route('/usuario/delete/<int:idUsuario>')
def delete_usuario(idUsuario):
    delete_user(idUsuario)
    return redirect(url_for('usuarios'))

@app.route('/usuario/edit/<int:idUsuario>', methods=['POST'])
def edit_usuario(idUsuario):
    usuario = request.form['usuario']
    clave = request.form['clave']
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    update_user(idUsuario, usuario, clave, nombre, direccion, telefono)
    return redirect(url_for('usuarios'))

if __name__ == '__main__':
    app.run(debug=True)