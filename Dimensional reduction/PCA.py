# Load dataset
df = pd.read_csv("heart_disease.csv")   
print("Dataset Shape:", df.shape)
print(df.head())
# Separate features and target
X = df.drop("target", axis=1)
y = df["target"]
# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
print("\nExplained Variance Ratio:", pca.explained_variance_ratio_)
# Plot PCA clusters
plt.figure(figsize=(7,5))
plt.scatter(X_pca[:,0], X_pca[:,1], c=y)
plt.title("PCA - 2D Cluster Visualization")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()
