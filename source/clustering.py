import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
from sklearn.preprocessing import normalize
from contextlib import redirect_stdout
import scipy
import streamlit as st

def main():
    # Sample TF-IDF data (replace with your actual data)
    data = [
        "document 1", "document 2", "document 3", "document 4",
        "document 5", "document 6", "document 7", "document 8",
        "document 9", "document 10"
    ]
    tfidf_matrix = pd.DataFrame({
        "word1": [0.042, 0.038, 0.048, 0.057, 0.057, 0.057, 0.057, 0.034, 0.057, 0.057],
        "word2": [0.218, 0.038, 0.048, 0.057, 0.057, 0.057, 0.057, 0.034, 0.057, 0.057],
        "word3": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # ... more words and documents
    })
    #pca(data)
    
def pca(data):

    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Create TF-IDF matrix
    tfidf_matrix = vectorizer.fit_transform(data)

    # Print TF-IDF matrix
    #print(tfidf_matrix.toarray())
    

    # Create and fit K-Means model
    num_clusters = 2
    kmeans = KMeans(n_clusters=num_clusters, random_state=0, n_init="auto")
    kmeans.fit(tfidf_matrix)

    # Reduce dimensions for visualization (optional)
    pca = PCA(n_components=2, svd_solver="arpack")
    reduced_data = pca.fit_transform(tfidf_matrix)
    
    #printing tfidf to a file
    with pd.option_context("display.max_rows", None):
        with open("tfidf.txt", "w") as file:
            with redirect_stdout(file):
                scipy.io.mmwrite("tfidf.txt", tfidf_matrix)
    # Visualize clusters
    plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=kmeans.labels_)
    plt.title("K-Means Clustering Visualization (PCA)")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.show()
    return kmeans.labels_

def normalized(data):

    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Create TF-IDF matrix
    tfidf_matrix = vectorizer.fit_transform(data)

    #normalize
    normalized_tfidf_matrix = normalize(tfidf_matrix, axis=0, norm='l2')

    tfidf_matrix = normalized_tfidf_matrix

    # Print TF-IDF matrix
    print(tfidf_matrix.toarray())

    # Create and fit K-Means model
    num_clusters = 2
    kmeans = KMeans(n_clusters=num_clusters, random_state=0, n_init="auto")
    kmeans.fit(tfidf_matrix)

    # Reduce dimensions for visualization (optional)
    pca = PCA(n_components=2, svd_solver="arpack")  # Explicit solver for sparse data
    reduced_data = pca.fit_transform(tfidf_matrix)
    print(tfidf_matrix)

    # Project centroids to reduced space first
    reduced_centroids = pca.transform(kmeans.cluster_centers_)

    # Inverse transform to original space
    original_centroids = pca.inverse_transform(reduced_centroids)

    # Visualize clusters and centroids in original space
    plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=kmeans.labels_)
    plt.scatter(original_centroids[:, 0], original_centroids[:, 1], marker='*', c='red', label='Centroids')
    plt.title("K-Means Clustering Visualization (PCA)")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.legend()
    plt.show()

    # Optional: Visualize centroids in reduced space
    # plt.scatter(original_centroids[:, 0], original_centroids[:, 1], marker='*', c='red', label='Centroids')
    # plt.title("K-Means Centroids in Reduced Space")
    # plt.xlabel("Principal Component 1")
    # plt.ylabel("Principal Component 2")
    # plt.legend()
    # plt.show()

    return

if __name__ == "__main__":
    main()
    