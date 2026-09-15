"""
Hierarchical Clustering - Simple Example
----------------------------------------------
We group a small set of 2D points into clusters using
Agglomerative (bottom-up) Hierarchical Clustering.
"""

# Step 1: Import the libraries we need
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

# Step 2: Create a small set of points that naturally form 2 groups
# (Same style of data as the k-Means example, for easy comparison)
data = {
    "X": [1, 2, 1.5, 8, 9, 8.5, 1, 9, 2, 8.5, 1.5],
    "Y": [1, 1.5, 2,   8, 8, 7.5, 2, 9, 1, 8.5, 1]
}
df = pd.DataFrame(data)

print("----- Data Points -----")
print(df)

# Step 3: Create the Agglomerative Clustering model
# We choose the number of clusters we want to end up with
k = 2
model = AgglomerativeClustering(n_clusters=k, linkage="ward")

# Step 4: Fit the model and get the cluster label for each point
# (fit_predict both trains the model and returns the cluster labels)
labels = model.fit_predict(df)

# Step 5: Add the cluster labels to our data
df["Cluster"] = labels

# Step 6: Display the clustered data
print("\n----- Points with Assigned Cluster -----")
print(df)

# Step 7: Plot the result
plt.figure(figsize=(6, 5))
colors = ["red", "blue", "green"]
for cluster_num in range(k):
    points = df[df["Cluster"] == cluster_num]
    plt.scatter(points["X"], points["Y"],
                color=colors[cluster_num], label=f"Cluster {cluster_num}")

plt.title(f"Agglomerative Hierarchical Clustering (K={k})")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.tight_layout()
plt.show()
