import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.title("Cloud-Based Smart Grid Demand-Side Management Platform")

st.subheader("Simulated Smart Meter Dashboard")

# Select Hour
hour = st.slider("Select Hour of the Day", 0, 23, 12)

# Dynamic Pricing Logic
if 18 <= hour <= 22:
    price = 8  # Peak price
    peak_status = "Peak Hour"
else:
    price = 4  # Normal price
    peak_status = "Normal Hour"

st.write(f"Current Hour: {hour}")
st.write(f"Status: {peak_status}")
st.write(f"Electricity Price: ₹{price} per kWh")

# Device Simulation
st.subheader("Smart Devices")

ac = st.checkbox("Air Conditioner (1.5 kW)")
ev = st.checkbox("EV Charger (3 kW)")
lights = st.checkbox("Lights (0.5 kW)")
fan = st.checkbox("Fan (0.2 kW)")

total_load = 0

if ac:
    total_load += 1.5
if ev:
    total_load += 3
if lights:
    total_load += 0.5
if fan:
    total_load += 0.2

# Load Control Logic
if peak_status == "Peak Hour" and ev:
    st.warning("EV Charging Disabled During Peak Hours")
    total_load -= 3

st.subheader("Power Consumption")

st.write(f"Total Load: {total_load} kW")

cost = total_load * price
st.write(f"Estimated Cost per Hour: ₹{cost}")

# Logging Data
log_data = {
    "Timestamp": datetime.now(),
    "Hour": hour,
    "Load (kW)": total_load,
    "Cost": cost
}

df = pd.DataFrame([log_data])
df.to_csv("energy_log.csv", mode='a', header=False, index=False)

st.success("System Running on Cloud Platform")