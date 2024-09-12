#why we need knn
#thorugh it we can train our model such that it can predict through it's past data available
#from our labelled data it will get the charactristics ans then based on that it will identify unlabelled item
# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)  # Target variable: species of the flowers

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the KNeighborsClassifier
# We are using 3 neighbors (k=3)
knn = KNeighborsClassifier(n_neighbors=3)

# Train the KNN model
knn.fit(X_train, y_train)

# Predict outcomes on the test set
y_pred = knn.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Let's see the first 10 predictions and the true values
print("Predictions:", y_pred[:10])
print("True values:", y_test[:10].values)
