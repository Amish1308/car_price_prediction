import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("linearregression.pkl", "rb"))

st.title("CAR price Prediction")

name = st.text_input("Car Name")
company = st.text_input("Company")
year = st.number_input("Year of Purchase", min_value=1990, max_value=2035, value=2015)
kms_driven = st.number_input("Kilometers Driven", min_value=0, value=30000)
fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG", "LPG", "Electric"]
)


if st.button("Predict"):
    input_df = pd.DataFrame([[name, company, year, kms_driven, fuel_type]],
                            columns=["name", "company", "year", "kms_driven", "fuel_type"])

    try:
        prediction = model.predict(input_df)
        st.success(f"Estimated Car Price: ₹ {int(prediction[0]):,}")

    except Exception as e:
        st.error("Prediction failed. Please check your input values.")
        st.write(e)