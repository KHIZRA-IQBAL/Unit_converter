# import streamlit as st

# def convert_units(value, unit_from ,unit_to):
#     conversions = {
#         "meters_kilometers":0.001,
#         "kilometers_meters":1000,
#         "grams_kilograms":0.001,
#         "kilograms_grams":1000
#     }


#     key = f"{unit_from}_{unit_to}"

#     if key in conversions:
#         conversion = conversions[key]
#         return value * conversion
#     else:
#         return "Conversion not available"


# st.title("Unit Converter")
# value = st.number_input("Enter a value", min_value=1.0, step=1.0)
# unit_from = st.selectbox("Select unit from:", ["meters", "kilometers", "grams", "kilograms"])
# unit_to = st.selectbox("Select unit to:", ["meters", "kilometers", "grams", "kilograms"])
# if st.button("Convert"):
#     result = convert_units(value, unit_from, unit_to)
#     st.write(f"Converted value:{value} {unit_from} is equal to {result} {unit_to}")

import streamlit as st

def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000
    }

    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return None  # Return None for unavailable conversions

# Streamlit App
st.set_page_config(page_title="Unit Converter", page_icon="📏", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 24px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stSelectbox>div>div>select {
        padding: 10px;
        border-radius: 5px;
    }
    .stNumberInput>div>div>input {
        padding: 10px;
        border-radius: 5px;
    }
    .stSuccess {
        color: #4CAF50;
        font-size: 18px;
        font-weight: bold;
    }
    .stError {
        color: #FF0000;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("📏 Unit Converter")
st.markdown("Convert between different units easily! Select your units and enter the value to get started.")

# Input fields
col1, col2 = st.columns(2)
with col1:
    value = st.number_input("Enter a value", min_value=1.0, step=1.0, format="%.2f")
with col2:
    unit_from = st.selectbox("Select unit from:", ["meters", "kilometers", "grams", "kilograms"])

unit_to = st.selectbox("Select unit to:", ["meters", "kilometers", "grams", "kilograms"])

# Convert button
if st.button("Convert", key="convert_button"):
    result = convert_units(value, unit_from, unit_to)
    if result is not None:
        st.success(f"✅ Converted value: **{value} {unit_from}** is equal to **{result:.4f} {unit_to}**")
    else:
        st.error("❌ Conversion not available for the selected units.")
