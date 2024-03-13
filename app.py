from flask import Flask, render_template, url_for, redirect, request, flash, session


class Alimento:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade


alimentos = []

app = Flask(__name__)
app.secret_key = '09UDSADS09Sj)(i*&&)'


@app.route('/')
def index():
    return render_template('index.html', titulo='Dieta', alimentos=alimentos)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo treino')


app.run(debug=True)
