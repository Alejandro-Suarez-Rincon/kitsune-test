# Prueba Tecnica Kitsune

## Indice
- [Orden de Carpetas](#orden-de-carpetas)
- [Guia de Inicio Rapido](#guia-de-inicio-rapido)

---

## Orden de Carpetas
```
.
├── api
├── docker-compose.yml
├── etl
└── README.md
```

### api
Se maneja todo el api con fastAPI para el punto #2.

### etl
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

