from sklearn.cluster import DBSCAN

dbscan = DBSCAN(eps=1.5, min_samples=10)

labels = dbscan.fit_predict(X_scaled)

df['DBSCAN_cluster'] = labels

print(df['DBSCAN_cluster'].value_counts())
