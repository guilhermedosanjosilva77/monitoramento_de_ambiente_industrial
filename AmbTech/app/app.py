import requests
import random

API_KEY = "KLQJTTBYNZ8H2EDP"
channel_id = 3305446


def send_data(temp, um):

    url = f"https://api.thingspeak.com/update?api_key={API_KEY}&field1={temp}&field2={um}"

    resposta = requests.get(url)

    print("temp: ", temp)
    print("um: ", um)
    print("Resposta API: ", resposta.text)
    print("----------------------------")


def gerar_dados():

    temp = round(random.uniform(20, 90), 2)
    um = round(random.uniform(50, 80), 2)

    return temp, um


def read_data():

    url = f"https://api.thingspeak.com/channels/{channel_id}/feeds.json?results=10"

    response = requests.get(url)

    data = response.json()

    # .get() busca a chave "feeds" no dicionário, e retorna [] se não encontrar
    feeds = data.get("feeds", [])

    ultimo = feeds[-1]  # pega o último item da lista (mais recente)

    print("ultima temp: ", ultimo["field1"])
    print("ultima umidade: ", ultimo["field2"])

    return feeds