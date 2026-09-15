# Part 2 – Clustering

## What is Clustering?

Clustering is an **unsupervised learning** technique. Unlike classification,
the data has **no predefined labels**. We simply give the computer the data,
and it groups similar items together into **clusters** on its own.

## Real-World Example

A shopping mall has data about customers' spending habits, but no labels
like "high spender" or "low spender". Clustering can automatically group
customers into segments based on how similar their spending behaviour is —
without ever being told in advance what the groups should be.

## Classification vs Clustering – The Key Difference

**Classification:** "We already know the categories (Pass/Fail, Spam/Not
Spam), and we train the model to predict them."

**Clustering:** "We don't know any categories. We want the computer to
discover natural groups in the data by itself."

## Comparison Table

| Classification | Clustering |
|---|---|
| Supervised | Unsupervised |
| Labels available | No labels |
| Predict class | Find groups |
| Example algorithm: Decision Tree | Example algorithm: k-Means |

## Algorithms Covered in this Section

1. **k-Means** – groups points into K clusters based on distance to cluster
   centers (centroids).
2. **Hierarchical Clustering** – builds a tree-like hierarchy of clusters by
   repeatedly merging the closest groups.

Open each subfolder for detailed explanations and runnable code.
