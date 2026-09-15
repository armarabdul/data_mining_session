"""
Hierarchical Clustering - Dendrogram Example
--------------------------------------------------
We use scipy to draw a dendrogram, which shows step by step
how individual points are merged into larger clusters.
"""

# Step 1: Import the libraries we need
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Step 2: Create a small, easy-to-follow dataset
# A small dataset keeps the dendrogram simple and readable
data = {
    "X": [1, 2, 1.5, 8, 9, 8.5, 5, 5.5],
    "Y": [1, 1.5, 2,  8, 8, 7.5, 4, 4.5]
}
df = pd.DataFrame(data)
labels_for_points = [f"P{i}" for i in range(len(df))]

print("----- Data Points -----")
print(df)

# Step 3: Calculate the linkage matrix
# This performs the step-by-step merging used in agglomerative clustering
# and records the order and distance of every merge.
# "ward" linkage tends to create evenly sized, compact clusters.
merge_info = linkage(df[["X", "Y"]], method="ward")

# Step 4: Draw the dendrogram
plt.figure(figsize=(8, 5))
dendrogram(
    merge_info,
    labels=labels_for_points,
    color_threshold=6   # points/clusters merged below this distance share a color
)

plt.title("Dendrogram - Hierarchical Clustering")
plt.xlabel("Data Points")
plt.ylabel("Distance Between Clusters")

# Step 5: Draw a horizontal line showing where we could "cut" the tree
# Everything below this line stays in separate clusters;
# crossing this line tells us how many clusters we would get.
plt.axhline(y=6, color="black", linestyle="--", label="Cut line")
plt.legend()

plt.tight_layout()
plt.show()

print("\nHow to read this dendrogram:")
print("1. Each point starts as its own cluster (bottom of the tree).")
print("2. The closest points/clusters are merged first (lowest merges).")
print("3. Merging continues upward until everything is one cluster.")
print("4. A horizontal cut line shows how many clusters you get:")
print("   count how many vertical lines the cut line crosses.")
