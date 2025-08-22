## https://www.datos.gov.co/api/v3/views/e97j-vuf7/query.json

import requests
import psycopg2
from psycopg2.extras import execute_values

DB_HOST = 'localhost'
DB_USER = 'user'
DB_PASSWORD = 'password'
DB_NAME = 'proyectos'

# Obtencion de datos
url = 'https://www.datos.gov.co/resource/e97j-vuf7.json'
params = {'$limit': 20}
headers = {"X-App-Token": "ENOPHRQYQirAkbZhjgFbQpcGk"}

response = requests.get(url, params=params, headers=headers)
response.raise_for_status()
data = response.json()

# Normalizar datos
registros = []
for item in data:
    registros.append({
        "fecha_publicacion": item.get("fecha_publicaci_n"),
        "pais_prision": item.get("pais_prisi_n"),
        "consulado": item.get("consulado"),
        "delito": item.get("delito"),
        "extraditado": item.get("extraditado_y_o_repatriado"),
        "situacion_juridica": item.get("situaci_n_jur_dica"),
        "genero": item.get("g_nero"),
        "grupo_edad": item.get("grupo_edad"),
        "cantidad": int(item.get("cantidad", 0)),
        "latitud": float(item.get("latitud")) if item.get("latitud") else None,
        "longitud": float(item.get("longitud")) if item.get("longitud") else None,
    })

# Almacenamiento de datos
conn = psycopg2.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    dbname=DB_NAME
)

cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS prisioneros (
    id SERIAL PRIMARY KEY,
    fecha_publicacion DATE,
    pais_prision TEXT,
    consulado TEXT,
    delito TEXT,
    extraditado TEXT,
    situacion_juridica TEXT,
    genero TEXT,
    grupo_edad TEXT,
    cantidad INT,
    latitud FLOAT,
    longitud FLOAT
);
""")

insert_query = """
INSERT INTO prisioneros (
    fecha_publicacion, pais_prision, consulado, delito, extraditado,
    situacion_juridica, genero, grupo_edad, cantidad, latitud, longitud
) VALUES %s
"""

values = [
    (
        r["fecha_publicacion"], r["pais_prision"], r["consulado"], r["delito"],
        r["extraditado"], r["situacion_juridica"], r["genero"], r["grupo_edad"],
        r["cantidad"], r["latitud"], r["longitud"]
    )
    for r in registros
]

execute_values(cur, insert_query, values)
conn.commit()

print(f"{len(registros)} registros insertados en base de datos")

cur.close()
conn.close()
