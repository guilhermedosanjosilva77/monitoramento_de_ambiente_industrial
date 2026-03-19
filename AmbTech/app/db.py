import mysql.connector

DB_HOST = "mysql"
DB_USER = "app_user"
DB_PASSWORD = "app_pass"
DB_NAME = "ambtech"


def conectar():

    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    return conn


def salvar_registros(feeds):

    conn = conectar()
    cursor = conn.cursor()

    for item in feeds:

        # ThingSpeak retorna: '2026-03-18T23:57:38Z'
        # MySQL espera:       '2026-03-18 23:57:38'
        data_hora = item["created_at"].replace("T", " ").replace("Z", "")

        cursor.execute(
            "INSERT INTO registros (data_hora, temperatura, umidade) VALUES (%s, %s, %s)",
            (data_hora, item["field1"], item["field2"])
        )

    conn.commit()
    cursor.close()
    conn.close()