# Naive Bayes

## 1. Concept

Naive Bayes is a classification algorithm based on **probability**. It uses
Bayes' Theorem to calculate the probability of each class given the input
features, and picks the class with the highest probability.

## 2. Real-World Example

Think about how email apps detect spam. Words like "free", "prize", or "win"
appear far more often in spam messages than in normal messages. Naive Bayes
uses the frequency of such words to calculate how *likely* a message is to
be spam.

## 3. When to Use It

- Spam detection and text classification.
- When you need a fast, simple baseline classifier.
- When features can reasonably be treated as independent of each other.

## 4. Basic Working Principle

- **Prior Probability:** How likely a class is *before* looking at any
  features (e.g. out of all past emails, 40% were spam).
- **Evidence:** The feature values of the new data point we want to
  classify (e.g. the words in a new email).
- **Prediction:** Naive Bayes combines the prior probability with how likely
  the observed features are for each class, and picks the class with the
  **highest resulting probability**.

## 5. Why is it called "Naive"?

It is called "naive" because it makes a simplifying (and technically
not-quite-true) assumption: that **all features are independent of each
other**. For example, it assumes "Hours Studied" and "Attendance" don't
affect each other at all. This assumption is rarely 100% true in real life,
but the algorithm still works surprisingly well in practice.

## 6. Python Implementation

- [`01_simple_example.py`](01_simple_example.py) – Predicts Pass/Fail using
  Hours Studied and Attendance, with `GaussianNB`.
- [`02_text_classification.py`](02_text_classification.py) – Classifies
  short text messages as Spam / Not Spam using `CountVectorizer` and
  `MultinomialNB`.

## 7. Important Parameters

- `GaussianNB()` – used for numeric (continuous) features, assumes they
  follow a normal (bell-curve) distribution.
- `MultinomialNB()` – used for count-based data, such as word counts in
  text classification.

## 8. Expected Output

The scripts print the dataset, train/test predictions, accuracy, and the
prediction for one new sample (a new student, or a new text message).

## 9. Common Student Questions

**Q: Why is it called "Naive"?**
Because it naively assumes all features are independent, which simplifies
the maths a lot even though it isn't perfectly true in real data.

**Q: Where is Naive Bayes commonly used?**
Spam filtering, sentiment analysis, news categorization, and other text
classification tasks.

**Q: Why does it work well for text?**
Text data has many features (words), and treating each word as
independent — while not perfectly accurate — still captures enough signal
(e.g. "free" and "prize" appearing together) to classify text well, and it
is very fast even with thousands of words.

**Q: What is prior probability in simple terms?**
It's the "starting guess" — the overall chance of each class before we look
at any specific details of the new example.

## 10. Practice Question

In `02_text_classification.py`, add two of your own example messages (one
spam-like, one normal) to the training data, and test the model on a new
message of your choice.
