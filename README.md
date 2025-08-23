# Prueba Tecnica Kitsune

## Indice
- [Orden de Carpetas](#orden-de-carpetas)
- [Guia de Inicio Rapido](#guia-de-inicio-rapido)
- [API](#API)
- [WEB](#WEB)

---

## Orden de Carpetas
```
.
├── api
├── docker-compose.yml
├── etl
├── web
├── img_doc
└── README.md
```

### Carpeta api
Se maneja todo el api con fastAPI para el punto #2.

### Carpeta etl
Se maneja el script necesario para consumir el api de `datos.gov.co` y almacenarlo en base de datos.

### Carpeta web
Se maneja el front end, con next.js para el punto #3.

### Carpeta img_doc
Se agregan las capturas pertenecientes a la documentacion.

### docker-compose.yml
Tiene la estructura de los contenedores `API` y `DB`


## Guia de Inicio Rapido
### API y DB
- Ejecutar `docker compose up --build` si es la priemera vez.
- Ejecutar `docker compose up` si ya existe el contenedor.

### WEB
- Ejecutar `npm install` si es la primera vez.
- Ejecutar `npm run dev`, si ya se ejecuto `npm install`.

### ETL
- Es necesario crear un entorno de desarrollo con python.
- Ejecutarlo con `source env/bin/activate`.
- Instalar las librerias necesarias con `pip install -r requirements.txt`.
- Ejecutar `script.py`.

## API
A travez de `http://127.0.0.1:8001/docs` o `http://127.0.0.1:8001/redoc`, se puede ver la funcionalidad de los endpoints e incluso porbarlos sin la necesidad de postman.

### Endpoints
- `/prisioneros/` -> Listar
- `/prisioneros/{prisionero_id}` -> Buscar por id
- `/prisioneros/fecha/{fecha}` -> Filtrar por fecha
- `/prisioneros/buscar/{palabra}` -> Filtar por palabra (delito cometido)

## WEB
Con next.js, un framework de react, se crea el front end, necesario que consume el `API` de `Fast API`.

### Intefaz
Al entrar en `http://localhost:3000/`, se obtiene:

1. Un buscador por delito cometido, (tiene que respetar mayusculas, tildes, etc).
2. Lista de la base de datos consultada, donde se pude ver a detalle el prisionero seleccionado.

![interfaz_principal](img_doc/interfaz_principal.png)

Al ver detalle del prisionero se obtiene

1. Detalle del prisionero.
2. Boton de regresar, para volver a la tabla de prisionero.

![detalle](img_doc/detalle.png)