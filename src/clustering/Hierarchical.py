from scipy.cluster.hierarchy import linkage, fcluster

Z = linkage(X_scaled, method='ward')

clusters = fcluster(Z, 3, criterion='maxclust')

df['Hierarchical_cluster'] = clusters

print(df['Hierarchical_cluster'].value_counts())
