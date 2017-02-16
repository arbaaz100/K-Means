# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 20:37:15 2017

@author: Arbaaz_Khan
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 11:28:16 2017

@author: Arbaaz_Khan
"""
#importing the modules
import csv
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
coord=[]
cntr=[]
lst=[]

#Opening the *.csv file in read mode
try:
    f = open('C:/Users\ASUS-PC\Desktop\k means\\xclara.csv', 'r')
    reader=csv.reader(f,delimiter=",")
    for i in reader:
        coord.append(i)

#Handling Exceptions
except IOError:
    print("File Not Found!!!")
    sys.exit()

l=len(coord)
    
#Converting the string list to float type list
for i in range(0,l):
    for j in range(0,2):
        coord[i][j]=float(coord[i][j])

#Entering the Values
print("Number of Clusters must be less than the number of elements in dataset")
print("Enter the number of Clusters :")
k=input()
k=int(k)

# setting the random points as centroids
for i in range(0,k):
    cntr.append(coord[i])

# measure euclidean distance of each point from centroid and assign each point a label
for i in range(0,l):
    dist=[]
    ind=0
    for j in range(0,k):
        dist1=((coord[i][0]-cntr[j][0])*(coord[i][0]-cntr[j][0])+(coord[i][1]-cntr[j][1])*(coord[i][1]-cntr[j][1]))
        dist1=math.sqrt(dist1)
        dist.append(dist1)
    ind=np.argmin(dist)
    coord[i].append(ind)

#Entering the Number of Iterations
print("Enter the number of Iterations : ")
itr=int(input())

for r in range(0,itr):
    cntr=[[k]*2 for i in range(k)]   # to reinitialise 2D centroid list
    
    # finding recalculated new mean of clusters
    for x in range(0,k):
        sumx=0
        sumy=0
        count=0
        for i in range(0,l):
            if coord[i][2]==x:
                sumx=sumx+coord[i][0]
                sumy=sumy+coord[i][1]
                count+=1
        meanx=sumx/count
        meany=sumy/count
        cntr[x]=[meanx,meany]


    # measure euclidean distance of each point from centroid and assign label
    for row in coord:   # To delete an extra label column due to the previous clustering
        del row[2]
    for i in range(0,l):
        dist=[]
        ind=0
        for j in range(0,k):
            dist1=((coord[i][0]-cntr[j][0])*(coord[i][0]-cntr[j][0])+(coord[i][1]-cntr[j][1])*(coord[i][1]-cntr[j][1]))
            dist1=math.sqrt(dist1)
            dist.append(dist1)
        ind=np.argmin(dist)
        coord[i].append(ind)    

#Plotting the Graph and assigning color
h={0:'red',1:'green',2:'yellow',3:'black',4:'blue',5:'orange',6:'violet',7:'grey',8:'brown',9:'pink',10:'cyan'}
for i in range(0,l):
    plt.scatter(coord[i][0],coord[i][1],color=h[coord[i][2]])
    
plt.show()
