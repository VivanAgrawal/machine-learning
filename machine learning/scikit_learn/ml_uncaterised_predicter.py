from sklearn.datasets import load_iris
# You import the load_iris function from Scikit-learn’s datasets module.
#This function loads the famous Iris flower dataset — it’s a built-in toy dataset perfect for practice.
from sklearn.model_selection import train_test_split
#You import train_test_split, a function that splits your data into training and testing sets.
from sklearn.ensemble import RandomForestClassifier
# You import RandomForestClassifier, a machine learning model that builds many decision trees and 
# combines their results — very powerful for classification tasks!
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# 📦 Load dataset
iris = load_iris()
X = iris.data  # Features: sepal & petal length/width
y = iris.target  # Labels: 0, 1, 2 => setosa, versicolor, virginica

# ✂️ Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) 
# You split your data:
#70% for training (X_train, y_train)
#30% for testing (X_test, y_test)
#random_state=42 ensures the same split every time you run the code (for reproducibility).

#  Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)
#You create a Random Forest model instance.
#Then, .fit() trains the model using the training data — it learns the patterns between features and labels.

#  Predict
y_pred = model.predict(X_test)
#You predict the labels for the test data — these are the model’s guesses based on what it learned.

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred) * 100)
print("Precision (macro avg):", precision_score(y_test, y_pred, average='macro') * 100)
print("Recall (macro avg):", recall_score(y_test, y_pred, average='macro') * 100)
print("F1 Score (macro avg):", f1_score(y_test, y_pred, average='macro') * 100)
#You evaluate the model:
#Compare the true labels (y_test) with the predicted labels (y_pred)
#Multiply by 100 to show the metrics as percentages (%).
#"macro" average means you calculate the metric independently for each class and then take the average (treating all classes equally).

# Predict new flower
sample = [[5.1, 3.5, 1.4, 0.2]]  # sepal & petal values

#sample_data = [
#    [5.1, 3.5, 1.4, 0.2],  # Setosa
#    [6.0, 2.9, 4.5, 1.5],  # Versicolor
#    [6.3, 3.3, 6.0, 2.5],  # Virginica        
#]

prediction = model.predict(sample)
print("\nPredicted Class:", iris.target_names[prediction[0]])
#You predict the class of a new flower:
#sample is a new flower’s measurements.
#model.predict(sample) guesses the class (e.g., 0, 1, or 2).
#iris.target_names[prediction[0]] translates the class number into the actual flower name (like "setosa").