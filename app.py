from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
from datetime import datetime
import sqlite3
import os

app = FastAPI()

# Set up static files and templates
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Database setup
db_file = "real_estate.db"

# Ensure the database file exists
if not os.path.exists(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE Property (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        location TEXT NOT NULL,
        size REAL NOT NULL,
        bedrooms INTEGER NOT NULL,
        bathrooms INTEGER NOT NULL,
        price REAL NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE PricePrediction (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        property_id INTEGER,
        predicted_price REAL NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(property_id) REFERENCES Property(id)
    )
    ''')
    # Seed data
    cursor.execute("INSERT INTO Property (location, size, bedrooms, bathrooms, price) VALUES ('New York', 1200, 3, 2, 750000)")
    cursor.execute("INSERT INTO Property (location, size, bedrooms, bathrooms, price) VALUES ('San Francisco', 900, 2, 1, 850000)")
    conn.commit()
    conn.close()

# Models
class Property(BaseModel):
    id: int
    location: str
    size: float
    bedrooms: int
    bathrooms: int
    price: float

class PricePrediction(BaseModel):
    id: int
    property_id: int
    predicted_price: float
    timestamp: datetime

# Routes
@app.get("/", response_class=HTMLResponse)
async def home():
    return templates.TemplateResponse("home.html", {"request": {}})

@app.get("/predict", response_class=HTMLResponse)
async def predict_page():
    return templates.TemplateResponse("predict.html", {"request": {}})

@app.get("/market-trends", response_class=HTMLResponse)
async def market_trends_page():
    return templates.TemplateResponse("market_trends.html", {"request": {}})

@app.get("/about", response_class=HTMLResponse)
async def about_page():
    return templates.TemplateResponse("about.html", {"request": {}})

@app.get("/contact", response_class=HTMLResponse)
async def contact_page():
    return templates.TemplateResponse("contact.html", {"request": {}})

@app.post("/api/predict")
async def predict_price(property: Property):
    # Mock prediction logic
    predicted_price = property.size * 500 + property.bedrooms * 10000 + property.bathrooms * 5000
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO PricePrediction (property_id, predicted_price) VALUES (?, ?)", (property.id, predicted_price))
    conn.commit()
    conn.close()
    return {"predicted_price": predicted_price}

@app.get("/api/properties", response_model=List[Property])
async def get_properties():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Property")
    properties = cursor.fetchall()
    conn.close()
    return [Property(id=row[0], location=row[1], size=row[2], bedrooms=row[3], bathrooms=row[4], price=row[5]) for row in properties]

@app.get("/api/trends")
async def get_trends():
    # Mock trends data
    trends = {
        "New York": [750000, 760000, 770000],
        "San Francisco": [850000, 860000, 870000]
    }
    return trends

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
