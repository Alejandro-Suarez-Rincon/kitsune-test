from sqlalchemy.orm import Session
import models, schemas

def get_prisioneros(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Prisionero).offset(skip).limit(limit).all()

def get_prisionero_by_id(db: Session, prisionero_id: int):
    return db.query(models.Prisionero).filter(models.Prisionero.id == prisionero_id).first()

def get_prisioneros_by_fecha(db: Session, fecha: str):
    return db.query(models.Prisionero).filter(models.Prisionero.fecha_publicacion == fecha).all()

def get_prisioneros_by_palabra(db: Session, palabra: str):
    return db.query(models.Prisionero).filter(models.Prisionero.delito.ilike(f"%{palabra}%")).all()

def create_prisionero(db: Session, prisionero: schemas.PrisioneroCreate):
    db_prisionero = models.Prisionero(**prisionero.dict())
    db.add(db_prisionero)
    db.commit()
    db.refresh(db_prisionero)
    return db_prisionero
