<div align="center">

Transaction Intelli-Clean
</div>
<div>
A smart web application that uses Natural Language Processing (NLP) to instantly clean up and categorize cryptic credit card transaction descriptions.

</div>
<br>
<br>
<div>
The Problem
</div>
When you look at a bank statement and seen a confusing transaction like PAYTM*UBER INDIA SYSTEMS PV GURGAON? It's hard to tell what it was for at a glance. This ambiguity confuses customers and can lead to unnecessary support calls and disputes.
<div>
The Solution
</div>
This project aims to solves that exact problem. It acts as a "Transaction Translator".
You give it the messy description, and it uses a machine learning model to instantly provide two simple, clean pieces of information:
The Category: e.g., "Travel", "Shopping", "Food & Dining"
The Merchant: e.g., "Uber", "Amazon"

This turns confusing financial data into human-readable information, demonstrating a clear path to improving the customer experience for any digital payment service.

<br>

<br>

<div>
How It Works
</div>
The application uses a two-step process to clean the data:

NLP for Categorization: A Naive Bayes classification model, trained on transaction data, predicts the most likely category. The text is converted into numerical vectors using a TfidfVectorizer which emphasizes unique, predictive keywords.

Logic for Merchant Extraction: A simple but effective keyword-matching logic scans the description to identify and extract the clean merchant name.



