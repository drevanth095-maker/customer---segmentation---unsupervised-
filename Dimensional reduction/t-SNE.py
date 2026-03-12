from sklearn.manifold import TSNE
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X_scaled)
# Plot t-SNE clusters
plt.figure(figsize=(7,5))
plt.scatter(X_tsne[:,0], X_tsne[:,1], c=y)
plt.title("t-SNE - 2D Cluster Visualization")
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.show()
