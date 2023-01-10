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
data = pd.read_csv("https://raw.githubusercontent.com/dinhyenhp01/dss/main/Cosmetic_products_sales_model.csv?token=GHSAT0AAAAAAB5HGBWPJM63MC34XHN73JKMY55RSWQ")

if st.checkbox('Show Training Dataframe'):
    data

st.subheader("Please fill information of Product:")

Category_Name_ID = st.slider("Category Name ID", 0, 8,1)
Qty = st.number_input("Quantity of Products: ")
Cash_Discount = st.slider("Cash Discount", 0, 100,10)
Amount_to_Customer = st.number_input("Amount to Customer: ")
Master_Category = st.slider("Master Category ", 1, 12, 1)
Rank = st.slider("Rank", 1, 52, 4)

