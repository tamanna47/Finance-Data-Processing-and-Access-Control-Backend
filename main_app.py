from fastapi import FastAPI
from database import Base, engine
import auth_routes
import financial_routes
import dashboard_routes
import user_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Finance Backend API")

@app.get("/")
def home():
    return {"message": "Finance Backend API is running successfully"}

app.include_router(auth_routes.router)
app.include_router(financial_routes.router)
app.include_router(dashboard_routes.router)
app.include_router(user_routes.router)