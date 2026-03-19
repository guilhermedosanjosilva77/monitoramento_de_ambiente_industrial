import requests
import random
import time
import pandas as pd

API_KEY = "KLQJTTBYNZ8H2EDP"

channel_id = 3305446

def send_data(temp, um):

    url = f"https://api.thingspeak.com/update?api_key=KLQJTTBYNZ8H2EDP&field1={temp}&field2={um}"

    resposta  = requests.get(url)

    print("temp: ", temp)
    print("um: ", um)

    print("Resposta API ", resposta.text)
    
    print("----------------------------")

while True:
    temp = round(random.uniform(20, 90),2)
    um = round(random.uniform(50, 80),2)

    send_data(temp, um)

    time.sleep(10)
    break

def read_data():

    url = f"https://api.thingspeak.com/channels/3305446/feeds.json?results=1"

    response = requests.get(url)

    data = response.json()

    last_data = data["feeds"][0]

    print("ultima temp: ", last_data["field1"])
    print("ultima umidade: ", last_data["field2"])


def read_last_ten():

    url = f"https://api.thingspeak.com/channels/3305446/feeds.json?results=10"

    response = requests.get(url)

    data = response.json()

    feeds = data["feeds"]

    df = pd.DataFrame(feeds)

    df = df[["created_at", "field1", "field2"]]

    df.columns = ["data_hora", "temperatura", "umidade"]
    print(df)

