import random

# Function to generate random sensor data
def generate_sensor_data():
    pm25 = random.uniform(0, 100)
    co = random.uniform(0, 5)
    no2 = random.uniform(0, 1)
    o3 = random.uniform(0, 0.1)
    return pm25, co, no2, o3

# Function to calculate the Air Quality Index (AQI)
def calculate_aqi(pm25, co, no2, o3):
    # Replace with your AQI calculation logic
    # This is a simplified example; use an appropriate formula for AQI calculation
    aqi = (pm25 + co + no2 + o3) / 4
    return aqi

# Function to classify air quality based on AQI
def classify_air_quality(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    elif aqi <= 200:
        return "Unhealthy"
import random
import time

# Function to generate random water quality data (pH and turbidity)
def generate_water_quality_data():
    pH = random.uniform(6.5, 8.5)
    turbidity = random.uniform(0, 5)
    return pH, turbidity

# Function to simulate water level data
def simulate_water_level():
    water_level = random.uniform(0, 100)
    return water_level

while True:
    # Generate water quality data
    pH, turbidity = generate_water_quality_data()
    
    # Simulate water level data
    water_level = simulate_water_level()

    # Output the results
    print("Water Quality:")
    print(f"pH: {pH}")
    print(f"Turbidity: {turbidity}")

    print("Water Level:")
    print(f"Water Level: {water_level}")

    # Set a time interval for data simulation (e.g., every 5 minutes)
    time.sleep(300)
