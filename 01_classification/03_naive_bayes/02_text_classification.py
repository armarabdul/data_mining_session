"""
Naive Bayes - Text Classification Example
----------------------------------------------
We classify short messages as Spam or Not Spam using
CountVectorizer (to convert text into word counts) and
Multinomial Naive Bayes.
"""

# Step 1: Import the libraries we need
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 2: Create a small dataset of messages
data = {
    "Message": [
        "Win a free prize now",
        "Meeting at 10 AM tomorrow",
        "Claim your reward today",
        "Please submit the assignment",
        "You have won a free lottery",
        "Lecture notes uploaded to the portal",
        "Congratulations you are selected for a free gift",
        "Project deadline is next Monday",
        "Get a free recharge instantly",
        "Reminder: submit your fee receipt",
        "Limited time offer, claim now",
        "Class is rescheduled to 3 PM"
    ],
    "Label": [
        "Spam", "Not Spam", "Spam", "Not Spam",
        "Spam", "Not Spam", "Spam", "Not Spam",
        "Spam", "Not Spam", "Spam", "Not Spam"
    ]
}
df = pd.DataFrame(data)

# Step 3: Display the data
print("----- Message Dataset -----")
print(df)

# Step 4: Separate features (X) and target (y)
X = df["Message"]
y = df["Label"]

# Step 5: Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Step 6: Convert text messages into numeric word-count features
# CountVectorizer builds a vocabulary and counts how often each word appears
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)   # learn vocabulary + counts
X_test_counts = vectorizer.transform(X_test)         # use same vocabulary

# Step 7: Create and train the Multinomial Naive Bayes model
model = MultinomialNB()
model.fit(X_train_counts, y_train)

# Step 8: Predict on the test data
y_pred = model.predict(X_test_counts)
print("\n----- Predictions on Test Data -----")
print("Actual:   ", list(y_test))
print("Predicted:", list(y_pred))

# Step 9: Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy on Test Data: {accuracy * 100:.2f}%")

# Step 10: Classify a brand-new message
new_message = ["Claim your free prize before it expires"]
new_message_counts = vectorizer.transform(new_message)
prediction = model.predict(new_message_counts)

print("\nNew message:", new_message[0])
print("Predicted Label:", prediction[0])
