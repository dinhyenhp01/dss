import streamlit as st
from predict_cost import predict
import numpy as np
 
st.title('Home price prediction')
 
st.write('---')
 
# area of the house
area = st.slider('Area of the house', 1000, 5000, 1500)
 
# no. of bedrooms in the house
bedrooms = st.number_input('No. of bedrooms', min_value=0, step=1)
 
# no. of balconies in the house
balconies = st.radio('No. of balconies', (0, 1, 2 , 3))
 
# how old is the house? (age)
age = st.number_input('How old is the house (in years)?', min_value=0, step=1)
 
if st.button('Predict House Price'):
    cost = predict(np.array([[area, bedrooms, balconies, age]]))
    st.text(cost[0])
