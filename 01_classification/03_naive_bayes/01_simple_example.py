"""
Naive Bayes - Simple Example
--------------------------------
We predict whether a student will PASS or FAIL based on
Hours Studied and Attendance, using Gaussian Naive Bayes.
"""

# Step 1: Import the libraries we need
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Step 2: Create a small dataset
data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8, 2, 6, 3, 7],
    "Attendance":    [40, 45, 50, 60, 70, 85, 90, 95, 55, 80, 48, 92],
    "Result":        ["Fail", "Fail", "Fail", "Fail", "Pass", "Pass",
                       "Pass", "Pass", "Fail", "Pass", "Fail", "Pass"]
}
df = pd.DataFrame(data)

# Step 3: Display the data
print("----- Student Dataset -----")
print(df)

# Step 4: Separate features (X) and target (y)
X = df[["Hours_Studied", "Attendance"]]
y = df["Result"]

# Step 5: Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Step 6: Create the Gaussian Naive Bayes model
# GaussianNB is used because our features (hours, attendance) are numeric
model = GaussianNB()

# Step 7: Train the model
model.fit(X_train, y_train)

# Step 8: Predict on the test data
y_pred = model.predict(X_test)
print("\n----- Predictions on Test Data -----")
print("Actual:   ", list(y_test))
print("Predicted:", list(y_pred))

# Step 9: Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy on Test Data: {accuracy * 100:.2f}%")

# Step 10: Predict for a brand-new student
new_student = pd.DataFrame({"Hours_Studied": [5], "Attendance": [75]})
prediction = model.predict(new_student)
print("\nNew student (Hours_Studied=5, Attendance=75) -> Predicted Result:",
      prediction[0])

# Bonus: show the predicted probability for each class
probabilities = model.predict_proba(new_student)
print("Predicted probabilities (Fail, Pass):", probabilities[0])
