import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("laptop_price_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("💻 Laptop Price Prediction App")

# --- Dropdowns and Inputs ---
brand = st.selectbox("Brand", ["Select Brand", "ASUS", "Lenovo", "HP", "Dell", "Acer", "MSI", "Apple", "Avita", "Huawei"])
processor_brand = st.selectbox("Processor Brand", ["Select Processor Brand", "Intel", "AMD", "M1"])
processor_name = st.selectbox("Processor Name", ["Select Processor", "Core i3", "Core i5", "Core i7", "Ryzen 5", "Ryzen 7", "M1", "Celeron Dual"])
processor_gen = st.selectbox("Processor Generation", ["Select Generation", "10th", "11th", "12th", "Not Available"])
ram_gb = st.number_input("RAM (GB)", min_value=2, max_value=64, value=8)
ram_type = st.selectbox("RAM Type", ["Select RAM Type", "DDR4", "DDR5", "LPDDR4", "LPDDR5"])
ssd = st.number_input("SSD (GB)", min_value=0, max_value=2000, value=512)
hdd = st.number_input("HDD (GB)", min_value=0, max_value=2000, value=0)
os = st.selectbox("Operating System", ["Select OS", "Windows", "Mac", "DOS"])
graphic_card_gb = st.number_input("Graphics Card (GB)", min_value=0, max_value=16, value=2)

# --- Encoding dictionaries (same order as training encoders) ---
brand_map = {"ASUS": 0, "Lenovo": 1, "HP": 2, "Dell": 3, "Acer": 4, "MSI": 5, "Apple": 6, "Avita": 7, "Huawei": 8}
processor_brand_map = {"Intel": 0, "AMD": 1, "M1": 2}
processor_name_map = {"Core i3": 0, "Core i5": 1, "Core i7": 2, "Ryzen 5": 3, "Ryzen 7": 4, "M1": 5, "Celeron Dual": 6}
processor_gen_map = {"10th": 0, "11th": 1, "12th": 2, "Not Available": 3}
ram_type_map = {"DDR4": 0, "DDR5": 1, "LPDDR4": 2, "LPDDR5": 3}
os_map = {"Windows": 0, "Mac": 1, "DOS": 2}

# --- Prediction logic ---
if st.button("Predict Price"):
    if (
        brand.startswith("Select") or
        processor_brand.startswith("Select") or
        processor_name.startswith("Select") or
        processor_gen.startswith("Select") or
        ram_type.startswith("Select") or
        os.startswith("Select")
    ):
        st.warning("⚠️ Please fill all the fields before predicting.")
    else:
        try:
            # Encode inputs
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

            # Predict
            prediction = model.predict(input_data)[0]
            st.success(f"💰 Estimated Laptop Price: ₹{int(prediction):,}")

        except Exception as e:
            st.error(f"Error in prediction: {e}")
