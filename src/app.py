from flask import Flask, render_template, redirect, session, request
from libreria.conexion import tirarDados, insertar_tiradas, sacarRegistro, insertar_usuario
import os

app = Flask(__name__)
app.secret_key = 'contraseña_secreta'


@app.route('/', methods=['GET', 'POST'])
def usuario():
    if request.method == 'POST':
        usuario = request.form.get('user')
        insertar_usuario(usuario)
        session['user'] = usuario
        dados = request.form.get('dados')
        session['dados'] = dados
        caras = request.form.get('caras')
        session['caras'] = caras
        return redirect('juego')
    return render_template('usuario.html')


@app.route('/juego',  methods=['GET', 'POST'])
def juego():
    mensaje = False
    if session:
        usuario = session['user']
        caras = int(session['caras'])
        dados = int(session['dados'])

        if 'historial' not in session:
            session['historial'] = []

        if request.method == 'POST':
            tirada = tirarDados(dados, caras)
            insertar_tiradas(tirada, usuario)
            session['tirada'] = tirada

        registro = sacarRegistro(usuario)
        print(registro)
        if registro[0] == None:
            mensaje = True
            return render_template('juego.html', mensaje = mensaje)
        else:
            session['historial'] = sacarRegistro(usuario)
        return render_template('juego.html')
    else:
        redirect('/')


@app.route('/salir')
def salir():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run('0.0.0.0', port=port, debug=True)
