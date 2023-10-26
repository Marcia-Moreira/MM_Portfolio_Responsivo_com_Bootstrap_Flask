# Importar a Biblioteca Flask e a render_template (renderiza uma pag navegador...)

from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# especifica e roda apenas se for app na main
if __name__ == '__main__':
    app.run(debug=True)
