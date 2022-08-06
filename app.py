import streamlit as st
import joblib
model = joblib.load('Spam Ham Detector(1)')
st.title('SPAM HAM DETECTOR')
ip = st.text_input("Enter your message")
op = model.predict([ip])
if st.button('Detect'):
  st.title(op[0])

  
  
