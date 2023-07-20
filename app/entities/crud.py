from sqlalchemy.orm import Session
from . import models, schemas

def get_history(db: Session, id: int):
    return db.query(models.History).filter(models.History.id == id).first()

def get_all_history(db: Session):
    return db.query(models.History).all()

def get_history_by_page(db: Session, page: int, size: int):
    return db.query(models.History).limit(size).offset((page - 1) * size).all()

def create_history(db: Session, history: schemas.History):
    db_history = models.History(query=history.query, result=history.result)
    db.add(db_history)
    db.commit()
    db.refresh(db_history)
    return db_history