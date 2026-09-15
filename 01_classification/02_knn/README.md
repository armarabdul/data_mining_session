# k-Nearest Neighbours (k-NN)

## 1. Concept

k-NN classifies a new data point by looking at the **k closest points** to
it in the training data, and assigning the **majority class** among those
neighbours.

## 2. Real-World Example

Think of moving into a new neighbourhood. If you want to guess what kind of
food your neighbours eat, you might ask your 3 or 5 nearest neighbours and
go with whatever the majority of them eat — that's exactly the idea behind
k-NN.

## 3. When to Use It

- When decision boundaries are irregular and simple rules don't fit well.
- When you have a reasonably small dataset (k-NN can be slow on very large
  data because it compares against every point).
- When the features are numeric and on similar scales.

## 4. Basic Working Principle

1. Choose a value of **K** (number of neighbours to look at).
2. Calculate the **distance** (usually straight-line/Euclidean distance)
   from the new point to every point in the training data.
3. Pick the **K nearest** points (smallest distances).
4. Use **majority voting** — whichever class appears most among those K
   neighbours becomes the prediction.

## 5. Python Implementation

- [`01_simple_example.py`](01_simple_example.py) – Classifies people into
  Underweight / Normal / Overweight using Height and Weight.
- [`02_knn_with_scaling.py`](02_knn_with_scaling.py) – Shows why feature
  scaling matters for k-NN, comparing results with and without
  `StandardScaler`.

## 6. Important Parameters

- `n_neighbors` (K) – how many neighbours to look at.
- `metric` – how distance is measured (default is Euclidean distance).

## 7. Expected Output

The scripts print the dataset, the train/test split, the predicted classes,
accuracy, and the prediction for one new data point. The scaling example
additionally compares predictions before and after scaling.

## 8. Common Student Questions

**Q: What does K mean?**
K is simply the number of nearby neighbours the algorithm looks at before
making a decision.

**Q: Why do we calculate distance?**
Distance tells us how "similar" two points are. Points that are close
together in feature space are assumed to be similar and likely belong to
the same class.

**Q: What happens if K = 1?**
The model simply copies the class of the single closest point. This can be
very sensitive to noise or outliers in the data.

**Q: What happens if K is too large?**
The model starts looking at points that are far away and not really similar,
which can blur the decision and reduce accuracy. A very large K can even
cause the model to always predict the overall majority class, ignoring the
new point's actual position.

**Q: Why is k-NN sensitive to feature scale?**
Because it uses distance. If one feature (e.g. Salary in thousands) has much
larger numbers than another (e.g. Age), it will dominate the distance
calculation even if it isn't actually more important. Scaling puts all
features on a comparable range so each one contributes fairly.

## 9. Practice Question

In `01_simple_example.py`, change the new data point's Height and Weight
values and re-run the program. Does the predicted category match what you
would expect?
