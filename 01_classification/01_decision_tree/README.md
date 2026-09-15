# Decision Tree

## 1. Concept

A Decision Tree is a classification model that looks like an upside-down
tree made of yes/no (or true/false) questions. Starting at the top, we keep
answering questions about the data until we reach a final answer.

## 2. Real-World Example

Think about how a doctor might diagnose a patient:

- Is the temperature high? → Yes → Is there a cough? → Yes → "Flu"
- Is the temperature high? → No → "Healthy"

This step-by-step questioning is exactly how a Decision Tree works.

## 3. When to Use It

- When you want a model that is easy to explain to non-technical people.
- When your data has a mix of simple yes/no or numeric conditions.
- When you want to visualize *why* a decision was made.

## 4. Basic Working Principle

- **Root Node:** The very first question at the top of the tree. It uses the
  feature that best separates the data.
- **Decision Node / Internal Node:** A question that splits the data further
  (e.g. "Is Study Hours > 4?").
- **Branch:** The path taken based on the answer (Yes/No, or a range of
  values).
- **Leaf Node:** The final box at the bottom of a branch that gives the
  answer/class (e.g. "Pass" or "Fail").

The tree is built by repeatedly picking the feature and condition that best
separates the classes, until the data in each branch is (mostly) pure —
meaning it mostly belongs to one class.

We do **not** need to calculate entropy/information gain by hand for this
class — `scikit-learn` does it for us. It is enough to understand the idea:
**the tree always tries to ask the most useful question first.**

## 5. Python Implementation

- [`01_simple_example.py`](01_simple_example.py) – A tiny Pass/Fail dataset
  using Age and Study Hours.
- [`02_realistic_example.py`](02_realistic_example.py) – A slightly bigger
  Age/Salary/Purchased dataset, with prediction for a brand-new person.

## 6. Important Parameters

- `criterion` – how the tree measures the quality of a split (`"gini"` or
  `"entropy"`). We use the default, `"gini"`.
- `max_depth` – maximum depth of the tree. Limiting depth keeps the tree
  small and easy to read (and avoids overfitting).
- `random_state` – fixes randomness so results are repeatable.

## 7. Expected Output

Running the scripts will print the dataset, the train/test split sizes, the
predicted class for the test data and a new sample, the accuracy of the
model, and a text-based view of the tree's decision rules.

## 8. Common Student Questions

**Q: Why is it called a "tree"?**
Because it branches out from a single root into multiple paths, just like a
real tree — except it is drawn upside down (root at the top).

**Q: What is the root?**
The first, topmost question in the tree — the feature that gives the best
initial split of the data.

**Q: What is a leaf?**
A final node at the bottom of a branch that no longer splits further — it
directly gives the predicted class.

**Q: How does the tree make a prediction for new data?**
It starts at the root, answers each question using the new data's feature
values, follows the matching branch, and repeats until it reaches a leaf.
The class written in that leaf is the prediction.

**Q: Why is a Decision Tree useful?**
It is easy to visualize and explain — anyone can follow the yes/no questions
from root to leaf and see exactly why a prediction was made.

## 9. Practice Question

Using the dataset in `01_simple_example.py`, add one new student record with
your own Age and Study Hours values. Predict manually (by looking at the
printed tree) whether they will Pass or Fail, then check your answer by
running the modified code.
