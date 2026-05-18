import streamlit as st
import pickle
import string
#load model in read only mode 
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
#text cleaning on user data
def clean_text(text):
    # convert lowercase
    text = text.lower()
    # remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # remove extra spaces
    text = " ".join(text.split())
    return text
#title of our user interface
st.title("SMS & Email Spam Detector")
#user selection box
option = st.selectbox(
    "Select Input Type",
    ["SMS", "Email"]
)
#if option is sms
if option == "SMS":
    message = st.text_area("Enter SMS")#get input
    if st.button("Check SMS"):
        # if user did not enter any thing 
        if message.strip() == "":
            st.warning("Please enter an SMS first!")
        else:
            # cleaninng on data
            clean_message = clean_text(message)
            #convert in numerical 
            vec = vectorizer.transform([clean_message])
            # predict result
            result = model.predict(vec)[0]
            # output
            if result == 1:
                st.error("Spam Message Detected!")
            else:
                st.success("Ham Message (Not Spam)")

#email checking
else:
    subject = st.text_input("Email Subject")
    body = st.text_area("Email Body")
    if st.button("Check Email"):
        # input validation on user input
        if subject.strip() == "" or body.strip() == "":
            st.warning("Please enter email completely!")
        else:
            # combine subject and body 
            full_text = subject + " " + body
            # cleaning data
            clean_email = clean_text(full_text)
            # conversion
            vec = vectorizer.transform([clean_email])
            # prediction
            result = model.predict(vec)[0]
            # output
            if result == 1:
                st.error("Spam Email Detected!")
            else:
                st.success("Ham Email (Not Spam)")