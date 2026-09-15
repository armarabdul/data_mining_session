"""
Classification - Practice Exercises
----------------------------------------
Try to solve each exercise yourself in the space provided.
The complete solutions are given as comments at the bottom of
this file - only look at them AFTER you have tried it yourself.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# =================================================================
# Exercise 1: Decision Tree
# -----------------------------------------------------------------
# Using the dataset below, build a Decision Tree that predicts
# Pass/Fail based on Age and Study_Hours.
# Steps: split X/y -> train/test split -> create model -> train ->
#        predict -> print accuracy
# =================================================================
data1 = {
    "Age":         [15, 16, 15, 17, 16, 18, 15, 17, 18, 16],
    "Study_Hours": [1,  6,  2,  7,  3,  8,  1,  5,  9,  2],
    "Result":      ["Fail", "Pass", "Fail", "Pass", "Fail",
                     "Pass", "Fail", "Pass", "Pass", "Fail"]
}
df1 = pd.DataFrame(data1)

# TODO: Write your code for Exercise 1 here


# =================================================================
# Exercise 2: k-NN
# -----------------------------------------------------------------
# Using the dataset below, use k-NN (with K = 3) to classify a
# person as "Underweight", "Normal", or "Overweight" based on
# Height and Weight.
# =================================================================
data2 = {
    "Height_cm": [150, 155, 160, 165, 170, 175, 180, 158, 168, 172],
    "Weight_kg": [40,  45,  50,  70,  65,  60,  90,  42,  55,  95],
    "Category":  ["Underweight", "Underweight", "Normal", "Overweight",
                  "Normal", "Normal", "Overweight", "Underweight",
                  "Normal", "Overweight"]
}
df2 = pd.DataFrame(data2)

# TODO: Write your code for Exercise 2 here


# =================================================================
# Exercise 3: Naive Bayes
# -----------------------------------------------------------------
# Using the dataset below, use Naive Bayes to classify a message
# as "Spam" or "Not Spam".
# =================================================================
data3 = {
    "Message": [
        "Win a free prize now",
        "Meeting at 10 AM tomorrow",
        "Claim your reward today",
        "Please submit the assignment",
        "You have won a free lottery",
        "Lecture notes uploaded to the portal",
    ],
    "Label": ["Spam", "Not Spam", "Spam", "Not Spam", "Spam", "Not Spam"]
}
df3 = pd.DataFrame(data3)

# TODO: Write your code for Exercise 3 here


# =================================================================
# SOLUTIONS (Try the exercises yourself before reading below!)
# =================================================================

# ----- Solution 1: Decision Tree -----
# X1 = df1[["Age", "Study_Hours"]]
# y1 = df1["Result"]
# X1_train, X1_test, y1_train, y1_test = train_test_split(
#     X1, y1, test_size=0.3, random_state=42)
# model1 = DecisionTreeClassifier(max_depth=3, random_state=42)
# model1.fit(X1_train, y1_train)
# pred1 = model1.predict(X1_test)
# print("Decision Tree Accuracy:", accuracy_score(y1_test, pred1))

# ----- Solution 2: k-NN -----
# X2 = df2[["Height_cm", "Weight_kg"]]
# y2 = df2["Category"]
# X2_train, X2_test, y2_train, y2_test = train_test_split(
#     X2, y2, test_size=0.3, random_state=42)
# model2 = KNeighborsClassifier(n_neighbors=3)
# model2.fit(X2_train, y2_train)
# pred2 = model2.predict(X2_test)
# print("k-NN Accuracy:", accuracy_score(y2_test, pred2))

# ----- Solution 3: Naive Bayes (Text) -----
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB
# X3 = df3["Message"]
# y3 = df3["Label"]
# vectorizer = CountVectorizer()
# X3_counts = vectorizer.fit_transform(X3)
# model3 = MultinomialNB()
# model3.fit(X3_counts, y3)
# new_msg = vectorizer.transform(["Claim your free reward"])
# print("Prediction:", model3.predict(new_msg))
