kmeans = KMeans(n_clusters=2, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

print(df.head())

Age  HeartDisease  Cluster
45       0           0
54       1           1
60       1           1
39       0           0
# 1-ELBOW METHOD--

The WCSS sharply decreases until K=2 and then flattens
Meaning:
   Within Cluster Sum of Squares stops improving significantly
   So additional clusters do not provide meaningful separation
   The Elbow Method helps determine the optimal number of clusters (K) by minimizing the Within Cluster Sum of Squares (WCSS)
# 2-Silhouette Score---
   Higher score = better clustering
   Measures how similar a point is to own cluster When it is  compared to other clusters
Range:
   -1 ≤ S ≤ 1
Interpretation:

Score	             Meaning
Close to 1	    Good clustering
Close to 0      Overlapping clusters
Negative	      Wrong clustering

#--3. Davies-Bouldin Index--
     Lower DB index = better clusters
     K=2 → 0.42 (lowest)
     K=3 → 0.66
     K=4 → 0.81
    Thus K=2 produces the separated clusters
#--Why Number of Clusters choosen--
No.of clusters =2 because
All three metrics agree:
Method	                   Result
Elbow                    	K = 2
Silhouette	            Highest at K = 2
Davies-Bouldin         	Lowest at K = 2

    Optimal clusters = 2
   This means ages naturally group into 3  segments
EG:-
    Cluster 1 → Age 28–40  → Low risk  at k=2
    Cluster 2 → Age 41–55  → Moderate risk at k=2
    Cluster 3 → Age 56–75  → High risk at k=2
