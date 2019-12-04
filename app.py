from flask import Flask, render_template, redirect, session, request
from libreria.conexion import insertar_usuario, tirarDados, insertar_tiradas, sacarRegistro
app = Flask(__name__)
app.secret_key = 'contraseña_secreta'


@app.route('/', methods=['GET', 'POST'])
def usuario():
    if request.method == 'POST':
        usuario = request.form.get('user')
        # insertar_usuario(usuario)
        session['user'] = usuario
        dados = request.form.get('dados')
        session['dados'] = dados
        caras = request.form.get('caras')
        session['caras'] = caras
        return redirect('juego')
    return render_template('usuario.html')


@app.route('/juego',  methods=['GET', 'POST'])
def juego():
    if session:
        usuario = session['user']
        caras = int(session['caras'])
        dados = int(session['dados'])
        tirada = tirarDados(dados, caras)
        insertar_tiradas(tirada, usuario)
        session['tirada'] = tirada
        session['historial'] = sacarRegistro(usuario)
        print(session['historial'])
        return render_template('juego.html')
    else:
        redirect('/')

# @app.errorhandler(404)


@app.route('/salir')
def salir():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)
