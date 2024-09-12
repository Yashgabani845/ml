# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)  # Features
y = iris.target  # Target (species)

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Support Vector Classifier (with a linear kernel)
svc = SVC(kernel='linear')

# Train the model
svc.fit(X_train, y_train)

# Predict the test set
y_pred = svc.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Visualize the decision boundaries (only using 2 features for visualization purposes)
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_train.iloc[:, 0], y=X_train.iloc[:, 1], hue=y_train, palette='Set1', s=100)

# Support vectors
plt.scatter(svc.support_vectors_[:, 0], svc.support_vectors_[:, 1], s=200, facecolors='none', edgecolors='k')
plt.title("SVM - Support Vectors with Decision Boundary")
plt.show()
