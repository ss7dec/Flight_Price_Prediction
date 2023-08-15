# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 18:31:13 2023

@author: aaari
"""
import streamlit as st
import joblib
st.title("Flight Price Prediction App")


distance=st.number_input("Enter the Distance in KM",min_value=0.00)


d_time = st.time_input("Select the Departure time in Hours")
total_minutes = d_time.hour * 60 + d_time.minute

d_time = total_minutes / 60.0



no_of_stops=st.slider('Enter the Number of Stops',min_value=0,max_value=3,value=0)


days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
d_of_week=st.selectbox("Select a day of the week", days_of_week)
days_of_week=days_of_week.index(d_of_week)



months_of_travel = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
month_of_travel=st.selectbox('Select the Month of Travel',months_of_travel)
months_of_travel=months_of_travel.index(month_of_travel)



fuel_price=st.number_input('Enter the Fuel Price in USD',min_value=0.00)

demand=st.radio('Enter the Demand',['Low','Medium','High'])
l_demand=0
m_demand=0
h_demand=1
if demand=='Low':
    l_demand=1
    m_demand=0
    h_demand=0
elif demand=='Medium':
    l_demand=0
    m_demand=1
    h_demand=0
else:
    l_demand=0
    m_demand=0
    h_demand=1
    
values=[[distance,d_time,no_of_stops,days_of_week,months_of_travel,fuel_price,l_demand,m_demand]]
if st.button('Predict Price'):
    model=joblib.load('bestperformingGD.pkl')
    y_p=model.predict(values)[0]
    # print()
    st.write(str(y_p))
    