"""
Decision Tree - Simple Example
--------------------------------
We predict whether a student will PASS or FAIL based on their
Age and Study Hours, using a Decision Tree Classifier.
"""

# Step 1: Import the libraries we need
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score

# Step 2: Create a small, manually-created dataset
data = {
    "Age":         [15, 16, 15, 17, 16, 18, 15, 17, 18, 16],
    "Study_Hours": [1,  6,  2,  7,  3,  8,  1,  5,  9,  2],
    "Result":      ["Fail", "Pass", "Fail", "Pass", "Fail",
                     "Pass", "Fail", "Pass", "Pass", "Fail"]
}
df = pd.DataFrame(data)

# Step 3: Display the data
print("----- Student Dataset -----")
print(df)

# Step 4: Separate features (X) and target (y)
# X = the columns used to make a prediction
# y = the column we want to predict
X = df[["Age", "Study_Hours"]]
y = df["Result"]

# Step 5: Split the data into training data and testing data
# Training data teaches the model, testing data checks how well it learned
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Step 6: Create the Decision Tree model
# max_depth keeps the tree small and easy to read on a projector
model = DecisionTreeClassifier(max_depth=3, random_state=42)

# Step 7: Train (fit) the model using the training data
model.fit(X_train, y_train)

# Step 8: Predict the results for the test data
y_pred = model.predict(X_test)
print("\n----- Predictions on Test Data -----")
print("Actual:   ", list(y_test))
print("Predicted:", list(y_pred))

# Step 9: Predict for a brand-new student
new_student = pd.DataFrame({"Age": [16], "Study_Hours": [5]})
new_prediction = model.predict(new_student)
print("\nNew student (Age=16, Study_Hours=5) -> Predicted Result:",
      new_prediction[0])

# Step 10: Calculate the accuracy of the model on test data
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy on Test Data: {accuracy * 100:.2f}%")

# Step 11: Display the tree as simple text rules
# This shows the root, the decision nodes, the branches and the leaves
print("\n----- Decision Tree Rules -----")
print(export_text(model, feature_names=["Age", "Study_Hours"]))
