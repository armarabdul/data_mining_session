# k-Means Clustering

## 1. Concept

k-Means groups data points into **K clusters**, where each cluster has a
center point called a **centroid**. Every point is assigned to the cluster
whose centroid is closest to it.

## 2. Real-World Example

A mobile network company wants to place K new towers to serve a city. It can
use k-Means to group customer locations into K clusters, and place a tower
at each cluster's centroid so it serves that group of customers well.

## 3. When to Use It

- When you want to discover natural groupings in numeric data.
- When you already have a rough idea of how many groups (K) you expect.
- When clusters are roughly round/blob-shaped.

## 4. Basic Working Principle

1. Choose the number of clusters, **K**.
2. Randomly place K centroids among the data.
3. **Assignment step:** Assign every point to its nearest centroid.
4. **Update step:** Move each centroid to the average position of the
   points assigned to it.
5. **Repeat** steps 3 and 4 until the centroids stop moving much
   (convergence).

## 5. Python Implementation

- [`01_simple_example.py`](01_simple_example.py) – Clusters a small set of
  2D points into groups, prints cluster labels and centroids, and plots the
  result.
- [`02_kmeans_visualization.py`](02_kmeans_visualization.py) – A clearer
  visualization comparing K=2 vs K=3, plus a simple elbow-method plot.

## 6. Important Parameters

- `n_clusters` (K) – the number of groups to form.
- `random_state` – fixes randomness so results are repeatable.
- `n_init` – number of times the algorithm runs with different starting
  centroids (scikit-learn keeps the best result).

## 7. Expected Output

The scripts print the original points, the assigned cluster label for each
point, and the centroid coordinates, followed by a scatter plot showing
points colored by cluster with centroids marked.

## 8. Common Student Questions

**Q: What does K mean?**
K is the number of clusters (groups) we want the algorithm to form. We
choose this number ourselves before running the algorithm.

**Q: What is a centroid?**
The centroid is the "center point" of a cluster — literally the average
position of all the points currently in that cluster.

**Q: How are points assigned to clusters?**
Each point is assigned to whichever centroid is closest to it (using
distance, usually Euclidean distance).

**Q: Why does the algorithm repeat?**
Because moving the centroids can change which centroid is nearest for some
points. The assign-and-update steps repeat until the centroids settle down
and stop changing — this is called convergence.

**Q: How do we choose the right K?**
One simple approach is the **elbow method**: try several values of K, plot
the "inertia" (how tightly packed each cluster is) against K, and look for
the point where the improvement starts to flatten out — like the bend of an
elbow.

## 9. Practice Question

In `01_simple_example.py`, change `n_clusters` from 2 to 3, re-run the
program, and observe how the grouping and the plotted centroids change.
