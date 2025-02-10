import streamlit as st
import pickle
import os

# Define the path to your model file
model_path = "model.pkl"  # Change this to your actual model file name

# Check if model file exists
if os.path.exists(model_path):
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)
else:
    st.error("Model file not found! Make sure it's in the correct directory.")
