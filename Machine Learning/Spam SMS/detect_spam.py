import streamlit as st
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

model = joblib.load('./model.pkl')
vectorizer = joblib.load('./vectorizer.pkl')

def classify_sms(sms):
    sms_tfidf = vectorizer.transform([sms])
    prediction = model.predict(sms_tfidf)
    return 'Spam' if prediction[0] == 1 else 'Ham'

st.title('SMS Spam Classifier')
st.write('Enter an SMS message to classify it as Spam or Ham.')
sms_input = st.text_area('Enter SMS message')

if st.button('Classify'):
    if sms_input:
        result = classify_sms(sms_input)
        st.write(f'The SMS is classified as: **{result}**')
    else:
        st.write('Please enter an SMS message.')
