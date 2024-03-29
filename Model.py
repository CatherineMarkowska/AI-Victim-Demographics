import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


#imports the data
data = pd.read_csv("demographics.csv")

data = data[["years spent at company","age"]]         
print(data)
#standardize the data
x_std = StandardScaler().fit_transform(data)

#the value of k has been defined for you
k = 5

#apply the kmeans algorithm
km = KMeans(n_clusters=k).fit(x_std) 

#get the centroid and label values
centroids = km.cluster_centers_
labels = km.labels_

#sets the size of the graph
plt.figure(figsize=(4,5))


#use a for loop to plot the data points in each cluster
for i in range(k):
    cluster = x_std[labels == i]
    plt.scatter(cluster[:,0], cluster[:,1])
    print(cluster)

y_new_inverse = x_std.inverse_transform(x_std)

#plot the centroids
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=100,
            c='r', label='centroid')
            
#shows the graph
plt.xlabel("years spent at company")
plt.ylabel("age")
plt.show()
