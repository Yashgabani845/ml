# Import required libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
# Sample dataset
data = {
    'Age': ['<=30', '<=30', '31-40', '>40', '>40', '>40', '31-40', '<=30', '<=30', '>40', '<=30', '31-40', '31-40', '>40'],
    'Income': ['High', 'High', 'High', 'Medium', 'Low', 'Low', 'Low', 'Medium', 'Low', 'Low', 'Medium', 'Medium', 'High', 'Medium'],
    'CreditScore': ['Fair', 'Excellent', 'Fair', 'Fair', 'Fair', 'Excellent', 'Excellent', 'Fair', 'Fair', 'Fair', 'Excellent', 'Excellent', 'Fair', 'Excellent'],
    'BuyProduct': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

# Convert to DataFrame
df = pd.DataFrame(data)
print(df)
# Convert categorical variables to numeric using pandas' get_dummies
X = pd.get_dummies(df[['Age', 'Income', 'CreditScore']], drop_first=True)
y = df['BuyProduct'].map({'Yes': 1, 'No': 0})  # Target variable (1 for Yes, 0 for No)
# Split dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
# Initialize the DecisionTreeClassifier
clf = DecisionTreeClassifier(criterion='entropy', random_state=0)

# Train the model
clf.fit(X_train, y_train)
# Predict outcomes on the test set
y_pred = clf.predict(X_test)
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
# Visualize the decision tree
import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))
tree.plot_tree(clf, filled=True, feature_names=X.columns, class_names=['No', 'Yes'])

plt.show()




#theory:
# decesion tree can solve both type of problems classification and regression
# classification tree : in this it has logical ifs for any two or three types of value
# important terms
# 1. Entropy : is measure of reandomness or unpredicatability in dataset
# 2. Information Gain : it is a measure of decrese in Entropy after a dataset split 
# exa: lets say first entropy was e1 after split entropy become e2 then gain = e1-e2
# 3.leaf node : it has classification of the decesion 
# 4. root node : top most node 
# formula of entropy : sum of all items(probability of that item come * log2(probability of that item come))
# we will choose that condition which will give us highest gain on split 