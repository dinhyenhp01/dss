import streamlit as st
import pandas as pd
import xgboost as xgb
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import  LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from pickle import load
from keras.models import load_model

st.header("Cosmetic Price Sales Product Prediction ")
data = pd.read_csv("https://github.com/dinhyenhp01/dss/blob/main/Cosmetic_products_sales_model.csv")

#load label encoder
encoder = LabelEncoder()
encoder.classes_ = np.load('classes.npy',allow_pickle=True)

# load model
rf_model = RandomForestRegressor(n_estimators=28,random_state=0)
rf_model = load_model("rf_regressor.json")

if st.checkbox('Show Training Dataframe'):
    data

st.subheader("Please fill information of Product:")

Category_Name_ID = st.slider("Category Name ID", 0, 8,1)
Qty = st.number_input("Quantity of Products: ")
Cash_Discount = st.slider("Cash Discount", 0, 100,10)
Amount_to_Customer = st.number_input("Amount to Customer: ")
Master_Category = st.slider("Master Category ", 1, 12, 1)
Rank = st.slider("Rank", 1, 52, 4)


if st.button('Price Prediction'):
    input_species = encoder.transform(np.expand_dims(inp_species, -1))
    inputs = np.expand_dims(
        [int(input_species), Category_Name_ID, Qty, Cash_Discount, Amount_to_Customer, Master_Category, Rank], 0)
    prediction = rf_model.predict(inputs)
    print("final pred", np.squeeze(prediction, -1))
    st.write(f"Price should be: {np.squeeze(prediction, -1):.2f}g")
