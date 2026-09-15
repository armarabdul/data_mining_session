# Mining Techniques – Classification and Clustering

This repository is a hands-on Python practical for the **MCA 2nd Year** course
at Moodalakatte Institute of Technology (MITK), Kandavara, Kundapura,
Karnataka. It is designed for a **2-hour classroom session** on two important
data mining techniques: **Classification** and **Clustering**.

Every example is small, uses a manually-created dataset, is fully commented,
and can be run on its own — perfect for demonstrating on a projector.

---

## 1. What is Data Mining?

Data Mining means finding useful patterns, relationships, or knowledge from
large amounts of data. Instead of a human going through data row by row, we
use algorithms that automatically discover patterns.

## 2. Why do we use Mining Techniques?

Real-world data (bank records, hospital records, student marks, customer
purchases) is too large for manual inspection. Mining techniques help us:

- Predict outcomes (Will this student pass or fail?)
- Group similar things together (Which customers behave similarly?)
- Make faster and smarter decisions from data

## 3. Overview of this Repository

```
Mining Techniques
        |
        +---- Classification (Supervised Learning)
        |       |
        |       +---- Decision Tree
        |       +---- k-NN
        |       +---- Naive Bayes
        |
        +---- Clustering (Unsupervised Learning)
                |
                +---- k-Means
                +---- Hierarchical Clustering
```

## 4. What is Classification?

Classification is a technique where we teach the computer using data that
already has **known answers (labels)**, so it can predict the answer for new,
unseen data.

Example: Using a student's **Age** and **Study Hours** to predict whether they
will **Pass** or **Fail**.

## 5. What is Clustering?

Clustering is a technique where the data has **no known labels**. The
computer looks at the data and groups similar items together on its own.

Example: Grouping customers into clusters based on their spending habits,
without knowing beforehand what those groups should be.

## 6. Supervised vs Unsupervised Learning

| Supervised Learning | Unsupervised Learning |
|---|---|
| Training data has known labels/answers | Training data has no labels |
| Goal: predict the label for new data | Goal: discover hidden groups/patterns |
| Example: Classification | Example: Clustering |

## 7. Classification vs Clustering

| Classification | Clustering |
|---|---|
| Supervised | Unsupervised |
| Labels available | No labels |
| Predict class | Find groups |
| Example algorithm: Decision Tree | Example algorithm: k-Means |

---

## 8. Repository Structure

```
mining_techniques/
│
├── 01_classification/
│   ├── 01_decision_tree/
│   ├── 02_knn/
│   └── 03_naive_bayes/
│
├── 02_clustering/
│   ├── 01_kmeans/
│   └── 02_hierarchical_clustering/
│
└── 03_practice/
```

Each algorithm folder has its own `README.md` explaining the concept, and two
Python programs: a very simple example and a slightly more advanced one.

---

## 9. Installation Instructions

### Step 1: Install Python

Make sure Python 3.8 or above is installed. Check with:

```bash
python --version
```

### Step 2: Create a Virtual Environment (recommended)

```bash
python -m venv venv
```

Activate it:

- **Windows:** `venv\Scripts\activate`
- **macOS/Linux:** `source venv/bin/activate`

### Step 3: Install the Requirements

```bash
pip install -r requirements.txt
```

---

## 10. How to Run Each Program

Every `.py` file runs independently. Simply navigate to the folder and run it
with Python. For example:

```bash
python 01_classification/01_decision_tree/01_simple_example.py
```

Run any file the same way — just change the path.

---

## 11. Suggested Order for Classroom Demonstration

1. Introduction (this README) – Classification vs Clustering
2. Decision Tree – `01_classification/01_decision_tree/`
3. k-NN – `01_classification/02_knn/`
4. Naive Bayes – `01_classification/03_naive_bayes/`
5. k-Means – `02_clustering/01_kmeans/`
6. Hierarchical Clustering – `02_clustering/02_hierarchical_clustering/`
7. Practice exercises – `03_practice/`

---

## 12. Expected Learning Outcomes

By the end of this session, students should be able to:

- Explain the difference between Classification and Clustering
- Explain the difference between Supervised and Unsupervised Learning
- Understand how a Decision Tree makes a decision
- Understand how k-NN classifies a point using nearby neighbours
- Understand the basic probability idea behind Naive Bayes
- Understand how k-Means groups data using centroids
- Understand how Hierarchical Clustering builds a dendrogram
- Write and run simple `scikit-learn` programs for each technique

---

## 13. Suggested 2-Hour Session Plan

| Time | Topic |
|---|---|
| 00–10 min | Introduction to Mining Techniques, Classification vs Clustering |
| 10–30 min | Decision Tree – Concept + simple Python implementation |
| 30–50 min | k-NN – Concept + implementation + why scaling matters |
| 50–70 min | Naive Bayes – Concept + simple implementation + text classification |
| 70–90 min | k-Means – Concept + implementation + visualization |
| 90–115 min | Hierarchical Clustering – Concept + implementation + dendrogram |
| 115–120 min | Quick recap + student questions |

---

## 14. Scope Note

This session covers **only** Classification (Decision Tree, k-NN, Naive
Bayes) and Clustering (k-Means, Hierarchical Clustering). Association Rule
Mining, Apriori, and related topics are **not** part of this session.
