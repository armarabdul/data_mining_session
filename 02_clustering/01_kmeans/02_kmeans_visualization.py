"""
k-Means - Visualization and Choosing K
-------------------------------------------
This example shows:
1. The original (unlabeled) points.
2. Clustering results for K=2 vs K=3, side by side.
3. A simple "elbow method" plot to help choose a good K.
"""

# Step 1: Import the libraries we need
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Step 2: Create a set of points that naturally form 3 groups
data = {
    "X": [1, 2, 1.5, 8, 9, 8.5, 4, 5, 4.5, 1, 9, 4.8],
    "Y": [1, 1.5, 2,  8, 8, 7.5, 1, 1.2, 0.8, 2, 9, 1.5]
}
df = pd.DataFrame(data)
print("----- Original Data Points -----")
print(df)

# ---------------------------------------------------------------
# Plot 1: Original points (no clustering yet, all one color)
# ---------------------------------------------------------------
plt.figure(figsize=(6, 5))
plt.scatter(df["X"], df["Y"], color="gray")
plt.title("Original Points (Before Clustering)")
plt.xlabel("X")
plt.ylabel("Y")
plt.tight_layout()
plt.show()

# ---------------------------------------------------------------
# Plot 2: Compare K=2 and K=3 side by side
# ---------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
colors = ["red", "blue", "green"]

for ax, k in zip(axes, [2, 3]):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(df[["X", "Y"]])
    labels = model.labels_
    centroids = model.cluster_centers_

    for cluster_num in range(k):
        points = df[labels == cluster_num]
        ax.scatter(points["X"], points["Y"],
                   color=colors[cluster_num], label=f"Cluster {cluster_num}")

    ax.scatter(centroids[:, 0], centroids[:, 1],
               color="black", marker="X", s=200, label="Centroids")
    ax.set_title(f"k-Means with K={k}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()

plt.tight_layout()
plt.show()

print("\nNotice how K=2 merges two groups into one cluster, while K=3")
print("correctly separates all three natural groups.")

# ---------------------------------------------------------------
# Elbow Method: plot inertia (within-cluster distance) vs K
# ---------------------------------------------------------------
# Inertia measures how tightly packed the points are within each cluster.
# It always decreases as K increases, but the improvement slows down
# after the "correct" number of clusters - forming an elbow shape.
inertia_values = []
k_values = range(1, 6)

for k in k_values:
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(df[["X", "Y"]])
    inertia_values.append(model.inertia_)

plt.figure(figsize=(6, 5))
plt.plot(list(k_values), inertia_values, marker="o")
plt.title("Elbow Method - Inertia vs K")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.xticks(list(k_values))
plt.tight_layout()
plt.show()

print("\nLook for the 'elbow' point where the curve bends and flattens.")
print("That point suggests a good value for K (here, around K=3).")
