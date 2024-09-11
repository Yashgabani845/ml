import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Sample dataset: square footage and house prices
X = np.array([1000, 1200, 1500, 1800, 2000]).reshape(-1, 1)  # square footage
y = np.array([150000, 200000, 300000, 350000, 400000])  # price

# Split the data into training and test sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Predict the house prices on the test data
y_pred = model.predict(X_test)

# Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"Predicted prices: {y_pred}")

# Visualizing the results
plt.scatter(X, y, color='blue')  # Actual data points
plt.plot(X, model.predict(X), color='red')  # Line of best fit
plt.title("Linear Regression: Square Footage vs Price")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.show()
