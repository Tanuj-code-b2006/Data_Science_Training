import streamlit as st
import numpy as np
import pickle
import sklearn

model = pickle.load(open("model.pkl","rb"))

st.title('🏠 House Pricing')

st.header("Pricing in Gurugram , Noida , Mumbai , Delhi ")

st.write("Enter The housing details below.")

square_feet = st.number_input("Square-Feet",  min_value=500,
    max_value=10000,
    value=500,
    step=100)

bedrooms= st.number_input("Bedrooms", min_value=1,
    max_value=10,
    value=1,
    step=1)

bathrooms = st.number_input("Bathrooms",  min_value=1,
    max_value=10,
    value=1,
    step=1)

if st.button("Predict The Housing Price"):
    features = np.array([[square_feet,bedrooms,bathrooms]])
    prediction = model.predict(features)

    st.success(f"Estimated House Price: ₹ {prediction[0]:,.2f}")
