import numpy as np
#NumPy is used for handling arrays and numerical operations in Python, which will help us store and manipulate the input data
import matplotlib.pyplot as plt
#Imports Matplotlib, a library used for data visualization. We will use it to plot a graph showing the relationship between square footage and house prices, and the regression line.

from sklearn.model_selection import train_test_split
#This imports the train_test_split function from the sklearn.model_selection module. It is used to split the dataset into training and testing sets. The training data is used to build the model, while the testing data is used to evaluate its performance.

from sklearn.linear_model import LinearRegression
#Imports the LinearRegression class from the sklearn.linear_model module. This class is used to create a linear regression model to predict continuous output (in this case, house prices).

from sklearn.metrics import mean_squared_error
#Imports the mean_squared_error function, which calculates the mean squared error (MSE) between the predicted and actual values. This helps evaluate how well our linear regression model is performing.

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
