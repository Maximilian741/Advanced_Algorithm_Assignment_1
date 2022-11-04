'''
Max Casteel
Software Assignment 1
11/3/2022
'''

'''
This program is an implementation of the Kruskal's algorithm for finding the minimum spanning tree of a weighted graph.
It utilizes (relatively) primitive data structures and operations to accomplish this task.
Furthermore, it uses a mergesort sorting algrotihm and a union-find data structure.
'''

import sys
import math
import random
import time
import matplotlib.pyplot as plt

class Graph:

    def init(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
   
   #Return the connected component of the element 'u' in 'S'
    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])

        
    
        T = findMinimumSpanningTree(self.graph)
    #combine the connected component given by node sets 'A' and 'B' into a single node set.
    def union(self,A,B):
        pass

    #Convert a set 'S' into a union-find data structure.
    def makeUnionFind(self, S):
        pass

    #Sort the values in array 'a' and return the sorted array 'b'.
    #implementation of a mergesort algorithm
    def mergeSort(a):
        #empty array to store sorted values
        b = []
        if len(a) > 1:
            #We need to find the middle of the array and also split it into two halves.
            mid = len(a) // 2
            lefthand = a[:mid]
            righthand = a[mid:]

            #Now we are going to recursively call mergeSort on both halves.
            mergeSort(lefthand)
            mergeSort(righthand)

            #Now we need to iterate through both sides and copy the sorted array back into the original array.
            #counter variables
            i = 0
            j = 0
            k = 0

            while i < len(lefthand) and j < len(righthand):
                if lefthand[i] < righthand[j]:
                    b[k] = lefthand[i]
                    i += 1
                else:
                    b[k] = righthand[j]
                    j += 1
                k += 1

            #Housekeeping to check if any elements were left over.
            while i < len(lefthand):
                b[k] = lefthand[i]
                i += 1
                k += 1

            while j < len(righthand):
                b[k] = righthand[j]
                j += 1
                k += 1

        return b


    '''
    This function takes in a graph and returns the minimum spanning tree of the graph.
    'A' is an NxN array of integers representing the graph.  A[i][j] is the weight of the edge between node i and node j.
    'T' must also be an adjancency matrix representation of the graph, but it will be the minimum spanning tree of the graph.
    '''
    def findMinimumSpanningTree(A):
        #T will store the resulting MST from the graph
        T = []
        self.graph = A

        i = 0;
        e = 0;


    