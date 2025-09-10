import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("laptop_price_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("💻 Laptop Price Prediction App")

# Essential inputs only
brand = st.selectbox("Brand", ["Select Brand", "ASUS", "Lenovo", "HP", "Dell", "Acer", "MSI", "Apple", "Avita", "Huawei"])
processor_brand = st.selectbox("Processor Brand", ["Select Processor Brand", "Intel", "AMD", "M1"])
processor_name = st.selectbox("Processor Name", ["Select Processor", "Core i3", "Core i5", "Core i7", "Ryzen 5", "Ryzen 7", "M1", "Celeron Dual"])
processor_gen = st.selectbox("Processor Generation", ["Select Generation", "10th", "11th", "12th", "Not Available"])
ram_gb = st.number_input("RAM (GB)", min_value=2, max_value=64, value=8)
ram_type = st.selectbox("RAM Type", ["Select RAM Type", "DDR4", "DDR5", "LPDDR4", "LPDDR5"])
ssd = st.number_input("SSD (GB)", min_value=0, max_value=2000, value=512)
hdd = st.number_input("HDD (GB)", min_value=0, max_value=2000, value=0)
graphic_card_gb = st.number_input("Graphics Card (GB)", min_value=0, max_value=16, value=2)
os = st.selectbox("Operating System", ["Select OS", "Windows", "Mac", "DOS"])

# Create dataframe with only essential features
input_data = pd.DataFrame([[
    brand, processor_brand, processor_name, processor_gen, ram_gb, ram_type,
    ssd, hdd, os, graphic_card_gb
]], columns=[
    "brand", "processor_brand", "processor_name", "processor_gnrtn", "ram_gb", "ram_type",
    "ssd", "hdd", "os", "graphic_card_gb"
])

# Predict button with validation
if st.button("Predict Price"):
    if any(val.startswith("Select") for val in input_data.iloc[0].astype(str).values):
        st.warning("⚠️ Please fill all the fields before predicting.")
    else:
        try:
            prediction = model.predict(input_data)[0]
            st.success(f"💰 Estimated Laptop Price: ₹{int(prediction):,}")
        except Exception as e:
            st.error(f"Error in prediction: {e}")
