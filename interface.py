import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.ensemble import RandomForestRegressor
from pickle import load
from tensorflow.keras.models import load_model


#Loading up the Random Forest Regression Model
rf_model = RandomForestRegressor(n_estimators=28,random_state=0)
rf_model.load_model('rf_regressor.json')

def predict(Category_Name, Qty, Cash_Discount, Amount_to_Customer, Master_to_Category, Rank):
	X_test = pd.DataFrame([[Category_Name, Qty, Cash_Discount, Amount_to_Customer, Master_to_Category, Rank]],
	columns = ['Category Name', 'Qty', 'Cash Discount', 'Amount to Customer', 'Master to Category', 'Rank'])
	X_new_test = poly.transform(X_test)
	X_new_test = pd.DataFrame(data = X_new_test, columns = poly.get_geature_names_out(X_test.columns))
	X_selector_test = selector.transform(X_new_test)
	X_test_res = scale.transform(X_selector_test)
	prediction = model.predict(X_test_res)
	return predict

st.set_page_config(page_title = "Cosmetic Sales Products Home Page")
st.title("Cosmetic Sales Products Home Page")
st.subheader('Predict Price Cosmetic Product Sales')
st.header('Fill information:')

Category_Name_ID = st.slider("Category Name ID", 0, 8,1)
Qty = st.number_input("Quantity of Products: ")
Cash_Discount = st.slider("Cash Discount", 0, 100,10)
Amount_to_Customer = st.number_input("Amount to Customer: ")
Master_Category = st.slider("Master Category ", 1, 12, 1)
Rank = st.slider("Rank", 1, 52, 4)

if st.button ('Predict Price'):
	price = predict(Category_Name, Qty, Cash_Discount, Amount_to_Customer, Master_to_Category, Rank)
	st.success(f'Predict Price of Cosmetic Product is: {Price[0]}')

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
