import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("laptop_price_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("💻 Laptop Price Prediction App")

# Define input fields (must match training features)
brand = st.selectbox("Brand", ["ASUS", "Lenovo", "HP", "Dell", "Acer", "MSI", "Apple", "Avita", "Huawei"])
processor_brand = st.selectbox("Processor Brand", ["Intel", "AMD", "M1"])
processor_name = st.selectbox("Processor Name", ["Core i3", "Core i5", "Core i7", "Ryzen 5", "Ryzen 7", "M1", "Celeron Dual"])
processor_gen = st.selectbox("Processor Generation", ["10th", "11th", "12th", "Not Available"])
ram_gb = st.number_input("RAM (GB)", min_value=2, max_value=64, value=8)
ram_type = st.selectbox("RAM Type", ["DDR4", "DDR5", "LPDDR4", "LPDDR5"])
ssd = st.number_input("SSD (GB)", min_value=0, max_value=2000, value=512)
hdd = st.number_input("HDD (GB)", min_value=0, max_value=2000, value=0)
os = st.selectbox("Operating System", ["Windows", "Mac", "DOS"])
os_bit = st.selectbox("OS Bit", ["32-bit", "64-bit"])
graphic_card_gb = st.number_input("Graphics Card (GB)", min_value=0, max_value=16, value=2)
weight = st.selectbox("Weight Category", ["Casual", "ThinNLight", "Gaming"])
warranty = st.selectbox("Warranty", ["No warranty", "1 year", "2 years"])
touchscreen = st.selectbox("Touchscreen", ["Yes", "No"])
msoffice = st.selectbox("MS Office", ["Yes", "No"])
rating = st.selectbox("Rating", ["1 star", "2 stars", "3 stars", "4 stars", "5 stars"])
num_ratings = st.number_input("Number of Ratings", min_value=0, value=100)
num_reviews = st.number_input("Number of Reviews", min_value=0, value=10)

# Create dataframe for model input
input_data = pd.DataFrame([[
    brand, processor_brand, processor_name, processor_gen, ram_gb, ram_type,
    ssd, hdd, os, os_bit, graphic_card_gb, weight, warranty,
    touchscreen, msoffice, rating, num_ratings, num_reviews
]], columns=[
    "brand", "processor_brand", "processor_name", "processor_gnrtn", "ram_gb", "ram_type",
    "ssd", "hdd", "os", "os_bit", "graphic_card_gb", "weight", "warranty",
    "Touchscreen", "msoffice", "rating", "Number of Ratings", "Number of Reviews"
])

# Predict button
if st.button("Predict Price"):
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"💰 Estimated Laptop Price: ₹{int(prediction):,}")
    except Exception as e:
        st.error(f"Error in prediction: {e}")
