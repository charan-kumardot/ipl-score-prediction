import streamlit as st
import pandas as pd
import pickle as pkl
import numpy as np  
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
filename = 'linear_model.pkl'
regressor = pkl.load(open(filename, 'rb'))
st.title('IPL 2020')
html_temp = """

<div style="background-color:yellow;padding:10px">
<h2 style="color:blue;text-align:center;">IPl score prediction</h2>
</div>
<div style="position:relative;top:0px;">
<h2 style="color:black;text-align:center;">created by Charan</h2>
</div>
"""

st.markdown('<style>body{background-color: red;}</style>',unsafe_allow_html=True)
st.markdown(html_temp,unsafe_allow_html=True)


batting_team = st.selectbox("select batting team",('select the batting_team','Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',
       'Mumbai Indians', 'Kings XI Punjab','Royal Challengers Bangalore', 'Delhi Daredevils', 'Sunrisers Hyderabad',
      ))

bowling_team = st.selectbox("select bowling team",('select the bowling_team','Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',
       'Mumbai Indians', 'Kings XI Punjab','Royal Challengers Bangalore', 'Delhi Daredevils','Sunrisers Hyderabad',
      ))

overs = st.number_input("overs above 5")
runs = st.number_input("current score ex:20")
wickets = st.number_input("current wicket ex:2")
runs_in_prev_5 = st.number_input("runs scored in previous 5 overs")
wickets_in_prev_5 = st.number_input("wickets in previous 5 overs")

def main(filename,regressor,batting_team,bowling_team,overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5):
        temp_array = list()
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif batting_team == 'Delhi Daredevils':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif batting_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            
            

        if bowling_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif bowling_team == 'Delhi Daredevils':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif bowling_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif bowling_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif bowling_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
        temp_array = temp_array + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
        print(temp_array)
        data = np.array([temp_array])
        print(data)
        filename = 'linear_model.pkl'
        regressor = pkl.load(open(filename, 'rb'))
        my_prediction = int(regressor.predict(data)[0])
        st.write("predicted score:", my_prediction)

    
    

if st.button('predict'):
    st.balloons()
    main(filename,regressor,batting_team,bowling_team,overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5)
