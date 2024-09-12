# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Sample dataset
data = {
    'word_freq_make': [0.21, 0.06, 0.00, 0.00, 0.90, 0.00],
    'word_freq_address': [0.28, 0.00, 0.00, 0.00, 0.00, 0.32],
    'word_freq_all': [0.50, 0.71, 0.35, 0.27, 0.00, 0.00],
    'word_freq_3d': [0.00, 0.00, 0.00, 0.14, 0.00, 0.00],
    'word_freq_our': [0.28, 0.14, 0.21, 0.00, 0.00, 0.28],
    'word_freq_over': [0.50, 0.07, 0.00, 0.14, 0.00, 0.14],
    'spam': [1, 1, 0, 0, 1, 0]  # 1 = Spam, 0 = Not Spam
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Features (X) and target (y)
X = df.drop('spam', axis=1)  # All columns except 'spam'
y = df['spam']  # The 'spam' column is the target

# Split the dataset into training and test sets (80% training, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Multinomial Naive Bayes model
nb = MultinomialNB()

# Train the model
nb.fit(X_train, y_train)

# Predict the labels for the test set
y_pred = nb.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Print the predictions and actual values
print(f"Predictions: {y_pred}")
print(f"True Values: {y_test.values}")
