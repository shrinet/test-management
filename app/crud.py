from sqlalchemy.orm import Session
from . import models, schemas
from hashlib import sha256

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = sha256(user.password.encode('utf-8')).hexdigest()
    db_user = models.User(username=user.username, email=user.email, full_name=user.full_name, password=hashed_password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_test(db: Session, test: schemas.TestCreate):
    db_test = models.Test(title=test.title)
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test

def create_question(db: Session, question: schemas.QuestionCreate):
    db_question = models.Question(test_id=question.test_id, text=question.text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question
