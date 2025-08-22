# Prueba Tecnica Kitsune

## Indice
- [Orden de Carpetas](#orden-de-carpetas)
- [Guia de Inicio Rapido](#guia-de-inicio-rapido)
- [API](#api)
---

## Orden de Carpetas
```
.
├── api
├── docker-compose.yml
├── etl
└── README.md
```

### Carpeta api
Se maneja todo el api con fastAPI para el punto #2.

### Carpeta etl
Se maneja el script necesario para consumir el api de `datos.gov.co` y almacenarlo en base de datos.

### docker-compose.yml
Tiene la estructura de los contenedores `API` y `DB`


## Guia de Inicio Rapido
### API y DB
- Ejecutar `docker compose up --build` si es la priemera vez.
- Ejecutar `docker compose up` si ya existe el contenedor.

### ETL
- Es necesario crear un entorno de desarrollo con python.
- Ejecutarlo con `source env/bin/activate`.
- Instalar las librerias necesarias con `pip install -r requirements.txt`.
- Ejecutar `script.py`.

## API
A travez de `http://127.0.0.1:8000/docs` o `http://127.0.0.1:8000/redoc`, se puede ver la funcionalidad de los endpoints e incluso porbarlos sin la necesidad de postman.

### Endpoints
- `/prisioneros/` -> Listar
- `/prisioneros/{prisionero_id}` -> Buscar por id
- `/prisioneros/fecha/{fecha}` -> Filtrar por fecha
- `/prisioneros/buscar/{palabra}` -> Filtar por palabra (delito cometido)