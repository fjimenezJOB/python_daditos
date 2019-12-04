from flask import Flask, render_template, redirect, session

app = Flask(__name__)

secret_key = 'contraseña_secreta'


@app.route('/')
def inicio():
    return render_template('usuario.html')
    


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug= True)