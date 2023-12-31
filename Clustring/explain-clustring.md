[Click here to open in Colab](https://colab.research.google.com/github/EzzOps/codespaces-blank/blob/main/main-clustering.ipynb)


1. **Import necessary libraries**: This is like gathering the tools you need. These tools include ways to organize data (pandas), create plots (matplotlib), group similar items together (KMeans from sklearn.cluster), standardize data (StandardScaler from sklearn.preprocessing), reduce the dimensionality of data (PCA from sklearn.decomposition), and calculate cosine similarity (cosine_similarity from sklearn.metrics.pairwise).

    ```python
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.preprocessing import StandardScaler
    from sklearn.cluster import KMeans
    from sklearn.decomposition import PCA
    from sklearn.metrics.pairwise import cosine_similarity
    ```

2. **Load the dataset**: This is like opening a book to read it. We're opening our dataset, which in this case is the "CC GENERAL.csv" file.

    ```python
    data = pd.read_csv("../input/CC GENERAL.csv")
    ```

3. **Handling Missing Values**: We're filling in missing values in the "MINIMUM_PAYMENTS" and "CREDIT_LIMIT" columns with their respective means.

    ```python
    data['MINIMUM_PAYMENTS'].fillna(data['MINIMUM_PAYMENTS'].mean(), inplace=True)
    data['CREDIT_LIMIT'].fillna(data['CREDIT_LIMIT'].mean(), inplace=True)
    ```

4. **Normalizing input values**: We're normalizing the input values by dropping the "CUST_ID" and "TENURE" columns and applying StandardScaler to the remaining features.

    ```python
    features = data.drop(['CUST_ID', 'TENURE'], axis=1)
    X = StandardScaler().fit_transform(features)
    ```

5. **Clustering using KMeans**: This is where we're grouping similar items together. We're applying KMeans clustering algorithm with 6 clusters to the normalized data.

    ```python
    kmeans = KMeans(n_clusters=6, random_state=42)
    data['cluster'] = kmeans.fit_predict(X)
    ```

6. **Visualization using PCA**: We're creating a plot to visualize our clusters. We're calculating cosine similarity, applying PCA to reduce the dimensionality of the distances, and plotting the clusters.

    ```python
    distances = 1 - cosine_similarity(X)
    X_pca = PCA(2).fit_transform(distances)
    plt.figure(figsize=(12, 8))
    for cluster in range(6):
        cluster_data = X_pca[data['cluster'] == cluster]
        plt.scatter(cluster_data[:, 0], cluster_data[:, 1], label=f'Cluster {cluster}')
    plt.title("Customer Segmentation based on Credit Card Usage (PCA)")
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend()
    plt.show()
    ```

The dataset was clustered into six groups using the K-Means algorithm, and the clusters were visualized using Principal Component Analysis (PCA). Now, let's interpret the clusters:

**Cluster 0: Diverse Spending Habits**
- People with average to high credit limits.
- Make a variety of purchases, including one-off and installment purchases.
- Generally active users with a mix of spending behaviors.

**Cluster 1: Cash Advance Users**
- More people with due payments who take cash advances more often.
- Potentially indicate a group of users who rely on cash advances and might have pending payments.

**Cluster 2: Installment Buyers**
- Less money spenders with average to high credit limits.
- Prefer making purchases in installments rather than lump sum payments.

**Cluster 3: High-Credit Cash Advances**
- People with high credit limits who frequently take cash advances.
- This group might have a higher financial capacity to access cash in advance.

**Cluster 4: High Spenders**
- High spenders with high credit limits.
- Make expensive purchases, indicating a potentially affluent customer segment.

**Cluster 5: Low-Spending Customers**
- People who don't spend much money but have average to high credit limits.
- This group consists of users with conservative spending habits.
