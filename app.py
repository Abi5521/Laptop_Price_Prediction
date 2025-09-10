import streamlit as st
import pandas as pd
import pickle

with open("laptop_price_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("💻 Laptop Price Prediction App")

brand_map = {"ASUS": 0, "Lenovo": 1, "HP": 2, "Dell": 3, "Acer": 4, "MSI": 5, "Apple": 6, "Avita": 7, "Huawei": 8}
processor_brand_map = {"Intel": 0, "AMD": 1, "M1": 2}
processor_name_map = {"Core i3": 0, "Core i5": 1, "Core i7": 2, "Ryzen 5": 3, "Ryzen 7": 4, "M1": 5, "Celeron Dual": 6}
processor_gen_map = {"10th": 0, "11th": 1, "12th": 2, "Not Available": 3}
ram_gb = st.number_input("RAM (GB)", min_value=2, max_value=64, value=8)
ram_type_map = {"DDR4": 0, "DDR5": 1, "LPDDR4": 2, "LPDDR5": 3}
ssd = st.number_input("SSD (GB)", min_value=0, max_value=2000, value=512)
hdd = st.number_input("HDD (GB)", min_value=0, max_value=2000, value=0)
os_map = {"Windows": 0, "Mac": 1, "DOS": 2}
graphic_card_gb = st.number_input("Graphics Card (GB)", min_value=0, max_value=16, value=2)

input_data = pd.DataFrame([[
    brand_map[brand],
    processor_brand_map[processor_brand],
    processor_name_map[processor_name],
    processor_gen_map[processor_gen],
    ram_gb,
    ram_type_map[ram_type],
    ssd,
    hdd,
    os_map[os],
    graphic_card_gb
]], columns=[
    "brand", "processor_brand", "processor_name", "processor_gnrtn", "ram_gb",
    "ram_type", "ssd", "hdd", "os", "graphic_card_gb"
])

if st.button("Predict Price"):
    if any(val.startswith("Select") for val in input_data.iloc[0].astype(str).values):
        st.warning("⚠️ Please fill all the fields before predicting.")
    else:
        try:
            prediction = model.predict(input_data)[0]
            st.success(f"💰 Estimated Laptop Price: ₹{int(prediction):,}")
        except Exception as e:
            st.error(f"Error in prediction: {e}")
