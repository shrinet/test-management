from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from .database import engine, SessionLocal
from . import models, schemas, crud, auth, dependencies, seeder

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    db = SessionLocal()
    try:
        seeder.create_admin_user(db)
    finally:
        db.close()

@app.post("/token", response_model=schemas.Token)
def login_for_admin(db: Session = Depends(dependencies.get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username, "role": user.role}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=schemas.UserCreate)
def create_user(user: schemas.UserCreate, db: Session = Depends(dependencies.get_db)):
    db_user = crud.create_user(db=db, user=user)
    return db_user

@app.post("/tests/", response_model=schemas.TestCreate)
def create_test(test: schemas.TestCreate, db: Session = Depends(dependencies.get_db), current_user: schemas.UserCreate = Depends(dependencies.get_current_admin_user)):
    db_test = crud.create_test(db=db, test=test)
    return db_test

@app.post("/questions/", response_model=schemas.QuestionCreate)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(dependencies.get_db), current_user: schemas.UserCreate = Depends(dependencies.get_current_admin_user)):
    db_question = crud.create_question(db=db, question=question)
    return db_question
