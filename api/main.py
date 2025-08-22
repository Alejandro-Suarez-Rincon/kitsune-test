from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Prisioneros")

# Dependencia para conexión con la BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/prisioneros/", response_model=list[schemas.Prisionero])
def listar_prisioneros(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_prisioneros(db, skip=skip, limit=limit)

@app.get("/prisioneros/{prisionero_id}", response_model=schemas.Prisionero)
def obtener_prisionero(prisionero_id: int, db: Session = Depends(get_db)):
    prisionero = crud.get_prisionero_by_id(db, prisionero_id)
    if not prisionero:
        raise HTTPException(status_code=404, detail="Prisionero no encontrado")
    return prisionero

@app.get("/prisioneros/fecha/{fecha}", response_model=list[schemas.Prisionero])
def filtrar_por_fecha(fecha: str, db: Session = Depends(get_db)):
    return crud.get_prisioneros_by_fecha(db, fecha)

@app.get("/prisioneros/buscar/{palabra}", response_model=list[schemas.Prisionero])
def filtrar_por_palabra(palabra: str, db: Session = Depends(get_db)):
    return crud.get_prisioneros_by_palabra(db, palabra)
