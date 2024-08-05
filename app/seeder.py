import bcrypt
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User

def create_admin_user(db: Session):
    email = "admin@example.com"
    password = "password"
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    # Check if the admin user already exists
    existing_user = db.query(User).filter_by(email=email).first()
    if existing_user:
        print("Admin user already exists")
        return
    
    admin_user = User(
        email=email,
        password=hashed_password,
        username="admin",
        full_name="Admin User",
        role="admin"
    )
    db.add(admin_user)
    db.commit()
    db.refresh(admin_user)
    print(f"Admin user created with email: {admin_user.email}")
