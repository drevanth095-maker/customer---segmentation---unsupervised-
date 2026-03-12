from sklearn.mixture import GaussianMixture

gmm = GaussianMixture(n_components=3, random_state=0)

gmm_labels = gmm.fit_predict(X_scaled)

df['GMM_cluster'] = gmm_labels

print(df['GMM_cluster'].value_counts())
