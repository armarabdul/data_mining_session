# Hierarchical Clustering

## 1. Concept

Hierarchical Clustering builds a **hierarchy (tree) of clusters** instead of
directly producing a fixed number of groups. The most common approach,
**Agglomerative Clustering**, starts with every point as its own tiny
cluster and repeatedly merges the two closest clusters until everything is
combined into one large cluster.

## 2. Real-World Example

Think about how living organisms are classified biologically: individual
species merge into genus, genus into family, family into order, and so on,
forming a tree-like hierarchy. Agglomerative clustering builds a similar
tree, but for any kind of numeric data.

## 3. When to Use It

- When you don't know the number of clusters in advance.
- When you want to see relationships between clusters at different levels
  (a whole hierarchy, not just one flat grouping).
- When the dataset is small to medium-sized (it does not scale well to
  very large datasets).

## 4. Basic Working Principle

1. **Start:** Treat every data point as its own individual cluster.
2. **Merge:** Find the two closest clusters and combine them into one.
3. **Repeat:** Keep merging the closest pair of clusters, step by step.
4. **Finish:** Continue until all points belong to a single big cluster,
   forming a complete hierarchy.

This is called **agglomerative** clustering because it works "bottom-up" —
starting small and agglomerating (combining) upward.

## 5. What is a Dendrogram?

A dendrogram is a tree diagram that shows the order and distance at which
clusters were merged. Reading it from the bottom (individual points) to the
top (one big cluster) shows exactly how the hierarchy was built.

We can decide how many clusters we want by drawing a **horizontal cut**
across the dendrogram: every vertical line the cut crosses represents one
resulting cluster.

## 6. Python Implementation

- [`01_simple_example.py`](01_simple_example.py) – Clusters the same style
  of 2D points as the k-Means example using `AgglomerativeClustering`.
- [`02_dendrogram.py`](02_dendrogram.py) – Draws a dendrogram using `scipy`
  and shows how to pick the number of clusters by cutting the tree.

## 7. Important Parameters

- `n_clusters` – the number of clusters to form (used by
  `AgglomerativeClustering`).
- `linkage` – how the distance between two clusters is measured (we use the
  default, `"ward"`, which tends to create evenly-sized clusters).

## 8. Expected Output

The scripts print data points with their assigned cluster, plot the
clustering result, and (in `02_dendrogram.py`) display a dendrogram with a
horizontal cut line.

## 9. Common Student Questions

**Q: What is a hierarchy?**
An arrangement of items into levels, where smaller groups combine to form
larger groups, layer by layer — like a family tree.

**Q: What is agglomerative clustering?**
The "bottom-up" method of hierarchical clustering: start with each point as
its own cluster and keep merging the closest pairs until one cluster
remains.

**Q: What is a dendrogram?**
A tree diagram showing the step-by-step merges made during hierarchical
clustering, along with the distance at which each merge happened.

**Q: How do we decide the number of clusters?**
By drawing a horizontal line across the dendrogram. The number of vertical
lines it crosses tells you how many clusters you get if you "cut" the tree
at that height. Cutting lower gives more, smaller clusters; cutting higher
gives fewer, larger clusters.

## 10. Practice Question

In `02_dendrogram.py`, try moving the horizontal cut line to a different
height (change the `color_threshold` value) and observe how the number of
resulting clusters changes.
