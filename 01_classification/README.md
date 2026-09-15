# Part 1 – Classification

## What is Classification?

Classification is a **supervised learning** technique. We give the computer
a dataset where the correct answer (label) is already known for every row.
The computer learns a pattern from this data, and then we use that pattern
to predict the label for new, unseen data.

## A Very Simple Example

Imagine we have data about students:

| Age | Study Hours | Result |
|---|---|---|
| 15 | 1 | Fail |
| 16 | 6 | Pass |
| 15 | 2 | Fail |
| 17 | 7 | Pass |

Here, **Age** and **Study Hours** are used to predict **Result** (Pass/Fail).

Another common example: using **Age** and **Income** to predict whether a
person will **Buy** or **Not Buy** a product.

## Important Terms

- **Features (X):** The input columns used to make a prediction (e.g. Age,
  Study Hours).
- **Target / Label (y):** The column we want to predict (e.g. Result).
- **Training Data:** The part of the data used to teach the model.
- **Testing Data:** The part of the data used to check how well the model
  learned (the model has not seen this data before).
- **Class:** One of the possible output categories (e.g. "Pass" or "Fail").
- **Prediction:** The class the model outputs for a new, unseen input.

## Why is Classification "Supervised" Learning?

Because the training data already has the correct answers (labels). The
computer is "supervised" by these known answers while learning, just like a
student learning from a teacher who already knows the correct answers.

## Algorithms Covered in this Section

1. **Decision Tree** – makes decisions using a tree of yes/no questions.
2. **k-NN (k-Nearest Neighbours)** – classifies a point based on its closest
   neighbours.
3. **Naive Bayes** – classifies using probability.

Open each subfolder for detailed explanations and runnable code.
