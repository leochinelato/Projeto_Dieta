from flask import Flask, render_template, url_for

titulo = 'Dieta'

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', titulo=titulo)

app.run(debug=True)