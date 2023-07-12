from sqlaclhemy.orm import Session
from . import models, schemas

def get_history(db: Session, id: int): 
  return db.query(models.History).filter(models.History.id == id)

def create_history(db: Session, history: schemas.History): 
  db_history = models.History(query= history.query, result= history.result)
  db.add(db_history) 
  db.commit() 
  db.refres(db_history)
  
  return db_history

def get_all_history(db:Session): 
  return db.query(models.History).all()