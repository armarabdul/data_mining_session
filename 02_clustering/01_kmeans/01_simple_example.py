"""
k-Means - Simple Example
----------------------------
We group a small set of 2D points into clusters using k-Means,
and visualize the resulting clusters and centroids.
"""

# Step 1: Import the libraries we need
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Step 2: Create a small set of points that naturally form 2 groups
data = {
    "X": [1, 2, 1.5, 8, 9, 8.5, 1, 9, 2, 8.5, 1.5],
    "Y": [1, 1.5, 2,   8, 8, 7.5, 2, 9, 1, 8.5, 1]
}
df = pd.DataFrame(data)

# Step 3: Display the points
print("----- Data Points -----")
print(df)

# Step 4: Create the KMeans model
# We choose the number of clusters (K) = 2, since we can see 2 groups
k = 2
model = KMeans(n_clusters=k, random_state=42, n_init=10)

# Step 5: Fit the model to the data (this runs the clustering algorithm)
model.fit(df)

# Step 6: Get the cluster label assigned to each point
df["Cluster"] = model.labels_

# Step 7: Get the coordinates of the cluster centers (centroids)
centroids = model.cluster_centers_

# Step 8: Print the results
print("\n----- Points with Assigned Cluster -----")
print(df)

print("\n----- Cluster Centers (Centroids) -----")
print(centroids)

# Step 9: Plot the clusters
plt.figure(figsize=(6, 5))
colors = ["red", "blue", "green"]
for cluster_num in range(k):
    cluster_points = df[df["Cluster"] == cluster_num]
    plt.scatter(cluster_points["X"], cluster_points["Y"],
                color=colors[cluster_num], label=f"Cluster {cluster_num}")

# Plot the centroids with a black X marker
plt.scatter(centroids[:, 0], centroids[:, 1],
            color="black", marker="X", s=200, label="Centroids")

plt.title(f"k-Means Clustering (K={k})")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.tight_layout()
plt.show()
