<div align="center">

Transaction Intelli-Clean
A smart web application that uses Natural Language Processing (NLP) to instantly clean up and categorize cryptic credit card transaction descriptions.

</div>

The Problem
Have you ever looked at a bank statement and seen a confusing transaction like PAYTM*UBER INDIA SYSTEMS PV GURGAON? It's hard to tell what it was for at a glance. This ambiguity confuses customers and can lead to unnecessary support calls and disputes.

The Solution
This project solves that exact problem. It acts as a "Transaction Translator".
You give it the messy description, and it uses a machine learning model to instantly provide two simple, clean pieces of information:
The Category: e.g., "Travel", "Shopping", "Food & Dining"
The Merchant: e.g., "Uber", "Amazon"

This turns confusing financial data into human-readable information, demonstrating a clear path to improving the customer experience for any digital payment service.

<br>
<div align="center">
<img src="https://www.google.com/search?q=https://i.imgur.com/8a3gYq1.png" alt="App Screenshot" width="700"/>
</div>
<br>

🛠️ How It Works
The application uses a two-step process to clean the data:

NLP for Categorization: A Naive Bayes classification model, trained on transaction data, predicts the most likely category. The text is converted into numerical vectors using a TfidfVectorizer which emphasizes unique, predictive keywords.

Logic for Merchant Extraction: A simple but effective keyword-matching logic scans the description to identify and extract the clean merchant name.

