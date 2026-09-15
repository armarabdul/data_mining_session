"""
k-NN - Why Feature Scaling Matters
--------------------------------------
k-NN uses distance to find neighbours. If one feature has much
bigger numbers than another, it will unfairly dominate the
distance calculation. This example shows the difference between
running k-NN WITHOUT scaling and WITH scaling.
"""

# Step 1: Import the libraries we need
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Step 2: Create a dataset with two features on VERY different scales
# Age is a small number (years), Salary is a big number (rupees)
data = {
    "Age":         [22, 25, 47, 52, 46, 56, 23, 27, 55, 48, 33, 45],
    "Salary":      [18000, 20000, 55000, 60000, 45000, 65000,
                    22000, 25000, 70000, 50000, 30000, 48000],
    "Purchased":   ["No", "No", "Yes", "Yes", "Yes", "Yes",
                    "No", "No", "Yes", "Yes", "No", "Yes"]
}
df = pd.DataFrame(data)

print("----- Dataset (Age and Salary have very different ranges) -----")
print(df)

X = df[["Age", "Salary"]]
y = df["Purchased"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# ---------------------------------------------------------------
# WITHOUT SCALING
# ---------------------------------------------------------------
# Here, Salary (thousands) completely overpowers Age in the distance
# calculation, because its numbers are much larger.
model_no_scaling = KNeighborsClassifier(n_neighbors=3)
model_no_scaling.fit(X_train, y_train)
pred_no_scaling = model_no_scaling.predict(X_test)
acc_no_scaling = accuracy_score(y_test, pred_no_scaling)

print("\n----- WITHOUT Scaling -----")
print("Predicted:", list(pred_no_scaling))
print("Actual:   ", list(y_test))
print(f"Accuracy: {acc_no_scaling * 100:.2f}%")

# ---------------------------------------------------------------
# WITH SCALING
# ---------------------------------------------------------------
# StandardScaler rescales every feature so it has mean 0 and a
# similar spread, so no single feature unfairly dominates distance.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # learn scale from training data
X_test_scaled = scaler.transform(X_test)         # apply the same scale to test data

model_scaled = KNeighborsClassifier(n_neighbors=3)
model_scaled.fit(X_train_scaled, y_train)
pred_scaled = model_scaled.predict(X_test_scaled)
acc_scaled = accuracy_score(y_test, pred_scaled)

print("\n----- WITH Scaling -----")
print("Predicted:", list(pred_scaled))
print("Actual:   ", list(y_test))
print(f"Accuracy: {acc_scaled * 100:.2f}%")

print("\nNote: On a bigger, more realistic dataset, the WITH-scaling")
print("version usually gives more reliable and fair results, because")
print("both Age and Salary are then given equal importance.")
