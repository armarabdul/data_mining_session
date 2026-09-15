"""
Decision Tree - Realistic Example
------------------------------------
We predict whether a person will PURCHASE a product based on
their Age and Salary, using a Decision Tree Classifier.
"""

# Step 1: Import the libraries we need
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score

# Step 2: Create a small dataset (Age, Salary in thousands, Purchased)
data = {
    "Age":       [22, 25, 47, 52, 46, 56, 23, 27, 55, 48, 33, 45],
    "Salary":    [18, 20, 55, 60, 45, 65, 22, 25, 70, 50, 30, 48],
    "Purchased": ["No", "No", "Yes", "Yes", "Yes", "Yes",
                  "No", "No", "Yes", "Yes", "No", "Yes"]
}
df = pd.DataFrame(data)

# Step 3: Display the data
print("----- Customer Dataset -----")
print(df)

# Step 4: Separate features (X) and target (y)
X = df[["Age", "Salary"]]
y = df["Purchased"]

# Step 5: Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Step 6: Create the Decision Tree model
model = DecisionTreeClassifier(max_depth=3, random_state=42)

# Step 7: Train the model
model.fit(X_train, y_train)

# Step 8: Predict on test data
y_pred = model.predict(X_test)
print("\n----- Predictions on Test Data -----")
print("Actual:   ", list(y_test))
print("Predicted:", list(y_pred))

# Step 9: Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy on Test Data: {accuracy * 100:.2f}%")

# Step 10: Predict for a brand-new person
# A 40-year-old person earning a salary of 42 (thousand)
new_person = pd.DataFrame({"Age": [40], "Salary": [42]})
prediction = model.predict(new_person)
print("\nNew person (Age=40, Salary=42k) -> Will Purchase?:", prediction[0])

# Step 11: Display the decision tree rules
print("\n----- Decision Tree Rules -----")
print(export_text(model, feature_names=["Age", "Salary"]))
