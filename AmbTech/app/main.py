from flask import Flask, render_template, redirect, url_for
import time
from app import send_data, gerar_dados, read_data
from db import salvar_registros

app = Flask(__name__)


@app.route("/")
def index():

    feeds = read_data()

    salvar_registros(feeds)

    return render_template("index.html", feeds=feeds)


@app.route("/enviar")
def enviar():

    temp, um = gerar_dados()

    send_data(temp, um)

    time.sleep(16)  

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)