# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Sample dataset: study hours and pass/fail outcomes
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)  # study hours
y = np.array([0, 0, 0, 1, 1, 1])  # pass (1) or fail (0)

# Split the data into training and test sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Logistic Regression model
model = LogisticRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Predict whether students will pass based on study hours in the test set
y_pred = model.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(f"Predicted outcomes: {y_pred}")

# Visualizing the results
plt.scatter(X, y, color='blue')  # Actual data points
plt.plot(X, model.predict_proba(X)[:, 1], color='red')  # Logistic curve
plt.title("Logistic Regression: Study Hours vs Pass/Fail")
plt.xlabel("Study Hours")
plt.ylabel("Pass Probability")
plt.show()
