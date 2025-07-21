# app.py
import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.datasets import load_iris

# Load model
with open("iris_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load feature names
iris = load_iris()
feature_names = iris.feature_names
target_names = iris.target_names

st.title("🌼 Iris Flower Species Prediction App")

st.markdown("Enter the flower measurements below to predict the species.")

# Input sliders
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.0)

# Collect input
input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# Predict
prediction = model.predict(input_data)
pred_proba = model.predict_proba(input_data)

# Output
st.subheader("Prediction:")
st.write(f"🌸 The predicted species is *{target_names[prediction[0]]}*.")

st.subheader("Prediction Probabilities:")
df_proba = pd.DataFrame(pred_proba, columns=target_names)
st.bar_chart(df_proba.T)

# Show raw input
with st.expander("Show input values"):
    st.write(pd.DataFrame(input_data, columns=feature_names))