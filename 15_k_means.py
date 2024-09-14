# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Generate synthetic data
n_samples = 300
n_clusters = 4
X, _ = make_blobs(n_samples=n_samples, centers=n_clusters, cluster_std=0.60, random_state=0)

# Apply K-means clustering
kmeans = KMeans(n_clusters=n_clusters, random_state=0)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# Create a DataFrame to store the data and labels
df = pd.DataFrame(X, columns=['Feature 1', 'Feature 2'])
df['Cluster Label'] = y_kmeans

# Write the DataFrame to a CSV file
csv_file_path = 'kmeans_clusters.csv'
df.to_csv(csv_file_path, index=False)

print(f"K-means clustering results saved to {csv_file_path}")