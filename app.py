import pandas as pd
import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler


with open('classifier_model.pkl', 'rb') as fid:
     model = pickle.load(fid)

st.title('Cardiovascular Risk Prediction App')

st.write('Enter some values for the following variables so that predictions can be made')

age = st.number_input('Enter the age',1,125)

selection = st.selectbox('Select your gender',('Male','Female'))
if selection=='Male':
    gender=1
else:
    gender=0

smoking = st.selectbox('Do you smoke or not',('Yes','No'))
if smoking=='No':
    is_smoking=0
else:
    is_smoking=1

cigs_per_day = st.number_input('If Yes,How many cigarattes do you smoke per day on average ?',0)

BP = st.selectbox('Do you take Blood Pressure Medications?',('Yes','No'))
if BP=='No':
    BPMeds=0
else:
    BPMeds=1

stroke = st.selectbox('Stroke prevalent in family history?',('Yes','No'))
if stroke=='No':
    prevalent_stroke=0
else:
    prevalent_stroke=1

hyp = st.selectbox('Hypertension prevalent in family history?',('Yes','No'))
if hyp=='No':
    hyper_tension=0
else:
    hyper_tension=1

dia = st.selectbox('Do you have diabetes',('Yes','No'))
if dia=='No':
    diabetes=0
else:
    diabetes=1

chol = st.number_input('Enter the cholestrol value(mg/dL)',100,500,format='%u')

sysbp = st.number_input('Enter your systolic blood pressure(mmHg)',0,300,format='%u')

diabp = st.number_input('Enter your diastolic blood pressure(mmHg)',0,200,format='%d')

bmi = st.number_input('Enter your Body Mass Index calculated as: Weight (kg) / Height(meter-squared)',10,40)

heart_rate = st.number_input('Enter your heart rate(Beats/min)')

glucose = st.number_input('total glucose mg/dL')

dataframe = pd.DataFrame([[age,gender,is_smoking,cigs_per_day,BPMeds,prevalent_stroke,hyper_tension,diabetes,chol,sysbp,diabp,bmi,heart_rate,glucose]])
st.write(dataframe)
 # Gives error because there is ony one value and mean and variance of that value is one only.so after transforming it

if st.button('Make Prediction'):
    prediction = model.predict(dataframe)
    if prediction == 1:
        st.subheader('Sorry to inform that you are at risk of coronary heart disease')
    else:
        st.subheader('Congrats!. You are not at risk of coronary heart disease')

