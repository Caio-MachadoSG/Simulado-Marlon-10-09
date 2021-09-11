from flask import Flask, render_template
from requests import get

app = Flask(__name__)


@app.route('/')
def promocoes():
    lista_promos = get("https://www.cheapshark.com/api/1.0/deals").json()
    lista_lojas = get("https://www.cheapshark.com/api/1.0/stores").json()
    tamanho_dados = len(lista_promos)

    return render_template("index.html", lista_promos=lista_promos, lista_lojas=lista_lojas, tamanho_dados=tamanho_dados)


if __name__ == '__main__':
    app.run()
