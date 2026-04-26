import streamlit as st
import pickle

# load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("SMS & Email Spam Detector")

option = st.selectbox("Select Input Type", ["SMS", "Email"])

if option == "SMS":
    message = st.text_area("Enter SMS")

    if st.button("Check"):
        vec = vectorizer.transform([message])
        result = model.predict(vec)[0]

        if result == 1:
            st.error("Spam !")
        else:
            st.success("Ham (not spam) ")

else:
    subject = st.text_input("Email Subject")
    body = st.text_area("Email Body")

    if st.button("Check"):
        full_text = subject + " " + body
        vec = vectorizer.transform([full_text])
        result = model.predict(vec)[0]

        if result == 1:
            st.error("Spam !")
        else:
            st.success("Ham (not spam )")