"""
k-NN - Simple Example
------------------------
We classify a person as Underweight, Normal, or Overweight
based on their Height and Weight, using k-Nearest Neighbours.
"""

# Step 1: Import the libraries we need
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Step 2: Create a small dataset
data = {
    "Height_cm": [150, 155, 160, 165, 170, 175, 180, 158, 168, 172, 148, 178],
    "Weight_kg": [40,  45,  50,  70,  65,  60,  90,  42,  55,  95,  38,  58],
    "Category":  ["Underweight", "Underweight", "Normal", "Overweight",
                  "Normal", "Normal", "Overweight", "Underweight",
                  "Normal", "Overweight", "Underweight", "Normal"]
}
df = pd.DataFrame(data)

# Step 3: Display the data
print("----- Height / Weight Dataset -----")
print(df)

# Step 4: Split into features (X) and target (y)
X = df[["Height_cm", "Weight_kg"]]
y = df["Category"]

# Step 5: Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Step 6: Create the k-NN model with K = 3
# The model will look at the 3 nearest neighbours to make a decision
model = KNeighborsClassifier(n_neighbors=3)

# Step 7: Train the model
model.fit(X_train, y_train)

# Step 8: Predict the categories for the test data
y_pred = model.predict(X_test)
print("\n----- Predictions on Test Data -----")
print("Actual:   ", list(y_test))
print("Predicted:", list(y_pred))

# Step 9: Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy on Test Data: {accuracy * 100:.2f}%")

# Step 10: Predict the category of a brand-new person
new_person = pd.DataFrame({"Height_cm": [162], "Weight_kg": [52]})

# Find the nearest neighbours and take the majority class among them
new_prediction = model.predict(new_person)
print("\nNew person (Height=162cm, Weight=52kg) -> Predicted Category:",
      new_prediction[0])
