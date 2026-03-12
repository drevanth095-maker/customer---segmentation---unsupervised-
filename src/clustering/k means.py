from sklearn.preprocessing import StandardScaler

X = df.drop('heart_disease', axis=1)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
#---- K Means-----
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=0)

kmeans_labels = kmeans.fit_predict(X_scaled)

df['KMeans_cluster'] = kmeans_labels

print(df['KMeans_cluster'].value_counts())
