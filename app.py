# app.py

import streamlit as st
import joblib
import re

# Load the pre-trained model
model = joblib.load('transaction_classifier_model.pkl')

# A simple (and effective) way to extract a known merchant name
# In a real system, this would be a much larger database of merchants
MERCHANT_KEYWORDS = {
    "Amazon": ["AMAZON", "AMZN"],
    "Flipkart": ["FLIPKART"],
    "Zomato": ["ZOMATO"],
    "Swiggy": ["SWIGGY"],
    "Uber": ["UBER"],
    "Ola": ["OLA"],
    "BookMyShow": ["BMS"],
    "Netflix": ["NETFLIX"],
    "Spotify": ["SPOTIFY"],
    "Indian Oil": ["INDIAN OIL"],
    "Bharat Petroleum": ["BHARAT PETROLEUM"],
    "BigBasket": ["BIGBASKET"],
    "JioMart": ["JIOMART"],
    "Zepto": ["ZEPTO"]
}

def extract_merchant(description):
    """Extracts a known merchant name from the description."""
    for merchant, keywords in MERCHANT_KEYWORDS.items():
        for keyword in keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', description.upper()):
                return merchant
    return "Unknown"


# --- Streamlit App UI ---

st.set_page_config(page_title="Transaction Intelli-Clean", layout="centered")

st.title("Transaction Intelli-Clean ✨")
st.write("Enter a cryptic credit card transaction description to instantly clean and categorize it.")

# Input text box
user_input = st.text_input("Enter Transaction Description:", "AMZN_STORE_#5523 BENGALURU")

# Classify button
if st.button("Categorize Transaction"):
    if user_input:
        # Predict the category using the ML model
        predicted_category = model.predict([user_input])[0]
        
        # Extract the merchant name
        cleaned_merchant = extract_merchant(user_input)
        
        # Display the results
        st.subheader("Results:")
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Predicted Category", value=predicted_category)
        with col2:
            st.metric(label="Cleaned Merchant", value=cleaned_merchant)

    else:
        st.warning("Please enter a transaction description.")