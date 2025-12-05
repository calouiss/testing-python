from fastapi import FastAPI

# Create a FastAPI application instance
app = FastAPI()

# Define an initial list of at least 4 cars as dictionaries
cars = [
    {"car_id": 1, "brand": "Toyota", "model": "Corolla", "available": True},
    {"car_id": 2, "brand": "Honda", "model": "Civic", "available": True},
    {"car_id": 3, "brand": "Ford", "model": "Focus", "available": False},
    {"car_id": 4, "brand": "Chevrolet", "model": "Malibu", "available": True},
]

# Endpoint to get the complete list of cars
@app.get("/cars")
def get_cars():
    return cars  # Returns the list of cars as JSON

# Endpoint to check the health status of the API
@app.get("/health")
def health_check():
    return {"status": "ok"}  # Returns a JSON object
