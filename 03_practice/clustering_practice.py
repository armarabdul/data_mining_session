"""
Clustering - Practice Exercises
------------------------------------
Try to solve each exercise yourself in the space provided.
The complete solutions are given as comments at the bottom of
this file - only look at them AFTER you have tried it yourself.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Shared dataset for all exercises: points forming 2-3 natural groups
data = {
    "X": [1, 2, 1.5, 8, 9, 8.5, 1, 9, 2, 8.5, 1.5],
    "Y": [1, 1.5, 2,   8, 8, 7.5, 2, 9, 1, 8.5, 1]
}
df = pd.DataFrame(data)

# =================================================================
# Exercise 1: k-Means with K = 2
# -----------------------------------------------------------------
# Use KMeans to find 2 groups in the dataset above.
# Print the cluster label for each point and the centroids.
# =================================================================

# TODO: Write your code for Exercise 1 here


# =================================================================
# Exercise 2: k-Means with K = 3
# -----------------------------------------------------------------
# Repeat Exercise 1, but this time use K = 3.
# Compare the new grouping with the K = 2 result. What changed?
# =================================================================

# TODO: Write your code for Exercise 2 here


# =================================================================
# Exercise 3: Hierarchical Clustering + Dendrogram
# -----------------------------------------------------------------
# Use AgglomerativeClustering to group the dataset into 2 clusters,
# then draw a dendrogram of the same data using scipy.
# =================================================================

# TODO: Write your code for Exercise 3 here


# =================================================================
# SOLUTIONS (Try the exercises yourself before reading below!)
# =================================================================

# ----- Solution 1: k-Means with K = 2 -----
# model1 = KMeans(n_clusters=2, random_state=42, n_init=10)
# model1.fit(df)
# print("Cluster labels:", model1.labels_)
# print("Centroids:", model1.cluster_centers_)

# ----- Solution 2: k-Means with K = 3 -----
# model2 = KMeans(n_clusters=3, random_state=42, n_init=10)
# model2.fit(df)
# print("Cluster labels:", model2.labels_)
# print("Centroids:", model2.cluster_centers_)

# ----- Solution 3: Hierarchical Clustering + Dendrogram -----
# model3 = AgglomerativeClustering(n_clusters=2, linkage="ward")
# labels3 = model3.fit_predict(df)
# print("Cluster labels:", labels3)
#
# merge_info = linkage(df[["X", "Y"]], method="ward")
# dendrogram(merge_info)
# plt.title("Dendrogram")
# plt.xlabel("Points")
# plt.ylabel("Distance")
# plt.show()
