#accurancy is higher and training time is less 
#application of random forest 
# 1. remote sesnsing
# 2. object detection 
# 3. tracking applications 
# in this we will provide the dataset and it will identify that objects and accordingn to that return 
#internally it uses multiple trees so overfittong will not occure in case of complex models
#it has high accurecy and ability to estimate the data
#in this every decesion tree will give some output and majority of the tree's output will be considered as a final output
# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)  # Target variable

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)  # n_estimators = number of trees

# Train the model (fit the random forest to the training data)
clf.fit(X_train, y_train)

# Predict outcomes on the test set
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Let's see the first 10 predictions and the true values
print("Predictions:", y_pred[:10])
print("True values:", y_test[:10].values)

# Feature Importance
importances = clf.feature_importances_
feature_names = X.columns
print("\nFeature importances:")
for name, importance in zip(feature_names, importances):
    print(f"{name}: {importance:.4f}")
