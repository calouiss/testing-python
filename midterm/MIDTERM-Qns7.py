# main.py
from fastapi import FastAPI

# Create FastAPI app
app = FastAPI(title="Car Rental API")

# Initial data: at least 4 cars with the required fields
cars = [
    {"car_id": 1, "brand": "Toyota",   "model": "Corolla", "available": True},
    {"car_id": 2, "brand": "Honda",    "model": "Civic",   "available": True},
    {"car_id": 3, "brand": "Ford",     "model": "Focus",   "available": False},
    {"car_id": 4, "brand": "Chevrolet","model": "Malibu",  "available": True},
]

# Optional root so "/" doesn't 404
@app.get("/")
def root():
    return {"endpoints": ["/cars", "/health", "/docs"]}

# GET /cars — return the full fleet (JSON)
@app.get("/cars")
def list_cars():
    return cars

# GET /health — return API health (JSON)
@app.get("/health")
def health():
    return {"status": "ok"}

# Allow running with `python main.py` (no uvicorn CLI needed)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
