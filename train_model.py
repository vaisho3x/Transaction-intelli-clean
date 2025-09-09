# train_model.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

print("Starting model training...")

# 1. Load the dataset
df = pd.read_csv('data/transactions.csv')

# 2. Define Features (X) and Target (y)
X = df['Description']
y = df['Category']

# 3. Create a machine learning pipeline
# This pipeline does two things:
#   a. TfidfVectorizer: Converts the messy text into numerical vectors.
#   b. MultinomialNB: A fast and effective text classification algorithm.
model = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', MultinomialNB())
])

# 4. Train the model on the entire dataset
model.fit(X, y)
print("Model training complete.")

# 5. Save the trained model to a file
joblib.dump(model, 'transaction_classifier_model.pkl')
print("Model saved to transaction_classifier_model.pkl")