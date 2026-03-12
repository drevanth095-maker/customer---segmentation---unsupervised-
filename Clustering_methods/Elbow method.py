#--load data--
df = pd.read_csv("heart_age.csv")
print(df.head())
#---features for clustering by using data--
X = df[['Age','HeartDisease']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
#----Elbow method----
wcss = []

for k in range(1,10):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,10), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()
