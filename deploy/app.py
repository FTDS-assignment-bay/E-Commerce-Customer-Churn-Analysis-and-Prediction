# Mengimpor library yang diperlukan
import streamlit as st
import pandas as pd
import joblib

# Tampilan judul halaman
st.markdown("========================================================================================")
st.markdown("<h1 style='text-align: center;'>Welcome to the Churn Prediction Model</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("========================================================================================")

# Menampilkan penjelasan anggota team dalam bentuk ekspander
with st.expander('Members'):
    st.caption('''
               |Name|Role|
               |---|---|
               |Saepul hilal|Data Engineering| 
               |Carlos Emmanuel Argado|Data Analysist|
               |Muhammad Insani|Data Scientist|
               |Akram Huwaidi Irnawan|Data Scientist|
               ''')

# Menampilkan keterangan
st.caption('Please enter the customer feature data input on the left side of your screen to get started!')

# Menampilkan penjelasan fitur input dalam bentuk ekspander
with st.expander('Input Feature Explanation '):
    st.caption('''
               |Feature|Explanation|
               |---|---|
               |Tenure | Tenure of customer in organization|
               |Complain | Any complaint has been raised in last month|
               |Day Since Last Order | Day Since last order by customer|
               |Cashback Amount | Average cashback in last month|
               |Number Of Device Registered | Total number of deceives is registered on particular customer|
               |Satisfaction Score | Satisfactory score of customer on service|
               |Prefered Order Cat | Preferred order category of customer in last month|
               |Marital Status | Marital status of customer|
               ''')

# Menampilkan sidebar untuk input data customer
st.sidebar.markdown("===================================")
st.sidebar.markdown("<h1 style='text-align: center;'>Input Data Customer</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("===================================")

# Fungsi untuk mendapatkan input dari pengguna
def user_input():
    tenure = st.sidebar.slider('Tenure', min_value=0, max_value=60, value=30)
    complain = st.sidebar.selectbox('Complain', ['none', 'any'])
    day_since_last_order = st.sidebar.slider('Days Since Last Order', min_value=0, max_value=365, value=30)
    cashback_amount = st.sidebar.slider('Cashback Amount', min_value=0, max_value=1000, value=500)
    number_of_device_registered = st.sidebar.slider('Number of Devices Registered', min_value=0, max_value=6, value=3)
    satisfaction_score = st.sidebar.slider('Satisfaction Score', min_value=1, max_value=5, value=3)
    prefered_order_cat = st.sidebar.selectbox('Preferred Order Category', ['Laptop & Accessory', 'Mobile', 'Mobile Phone', 
                                                             'Others','Fashion', 'Grocery'])
    marital_status = st.sidebar.selectbox('Marital Status', ['Single', 'Married', 'Divorced'])
    
    if complain == 'none' :
        complain = 0
    else :
        complain = 1
    
    data = {
        'tenure': tenure,
        'complain' : complain,
        'day_since_last_order': day_since_last_order,
        'cashback_amount': cashback_amount,
        'number_of_device_registered': number_of_device_registered,
        'satisfaction_score': satisfaction_score,
        'prefered_order_cat': prefered_order_cat,
        'marital_status': marital_status,
    }
    
    features = pd.DataFrame(data, index=[0])        
    return features

# Menjalankan fungsi input pengguna
input = user_input()

# Menampilkan hasil input pengguna dalam bentuk tabel
st.markdown("<h2 style='text-align: left;'>User Input Result</h2>", unsafe_allow_html=True)
st.table(input)

# Memuat model yang telah disimpan sebelumnya
load_model = joblib.load("model_xgb.pkl")

# Tombol untuk memprediksi
if st.button("Predict", help='Click me!'):
    # Melakukan prediksi menggunakan model
    prediction = load_model.predict(input)

    # Menampilkan hasil prediksi
    if prediction == 1:
        prediction = 'The customer is likely to churn'
    else:
        prediction = 'The customer is likely to stay'

    st.markdown("<h4 style='text-align: center;'>Based on the information provided by the user, the model predicts:</h4>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center;'>{prediction}</h1>", unsafe_allow_html=True)
    
    # Menampilkan hasil tambahan jika input termasuk dalam salah satu jenis fraud
    if prediction != "The customer is likely to stay":
        st.warning('This customer falls into the churn category. Please take appropriate action to retain the customer')
