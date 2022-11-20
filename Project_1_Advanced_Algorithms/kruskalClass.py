#Max Casteel
#Programming Assignment 1 - Uninon find adjacency matrix to find MST using Kruskals algorithm.
#Advanced Algorithms

import numpy as np
 #import numpy for matrix operations

class kruskalClass:

    #s = find(u,v)
    #Input: 'u' is a union-find structure.  'v' is a numerical index of a graph node.
    #Output: 's' is the muerical value corresponding to the label for the set of connected nodes to which 'v' belongs.
    def find(self,u,v):
        if u[v][0] == v:
            return v
        else:
            return self.find(u,u[v][0])

    #u_out = union(u_in,s1,s2)
    #Input: 'u_in' is a union-find data structure. 's1' and 's2' are numerical values
    #coresponding to the labels of two groups of graph nodes.
    #Output: 'u_out' is a union-find data structure that is the result of merging the two sets of nodes.
    def union(self,u_in,s1,s2):
        if u_in[s1][1] > u_in[s2][1]:
            u_in[s2][0] = s1
            return u_in
        elif u_in[s1][1] < u_in[s2][1]:
            u_in[s1][0] = s2
            return u_in
        else:
            u_in[s2][0] = s1
            u_in[s1][1] += 1
            return u_in
    
    #u = makeUnionFind(N)
    #Input: 'N' is the number of nodes in a graph.
    #Output: 'u' is a 1xN python dictionary, where the keys are numerical labels
    #for the nodes, and the values are numpy arrays with the 0th entry being a pointer 
    #to a node in the same dictionary.  The numpy arrays can be more than one 1-D if you want, but they must be numpy
    #arrays, and the 0th entry must contain pointers to other nodes that are used
    #in the 'find' and 'union' functions.
    def makeUnionFind(self,N):
        u = {}
        for i in range(N):
            u[i] = [i,0]
        return u

    #b = mergesort(a)
    #Input: 'a' is a 1xK numpy array.
    #Output: 'b' is a 1xK numpy array with elements in ascending order. (ie. b[0] <= b[1] <= ... <= b[K-1], lowest value to highest value)
    def mergesort(self,a):
        if len(a) > 1:
            mid = len(a)//2
            left = a[:mid]
            right = a[mid:]
            self.mergesort(left)
            self.mergesort(right)
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i][2] < right[j][2]:
                    a[k] = left[i]
                    i += 1
                else:
                    a[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                a[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                a[k] = right[j]
                j += 1
                k += 1
        return a

    #T = findMinimumSpanningTree(A)
    #Input: 'A' is an NxN numpy array representing an adjacency matrix for a graph.
    #If A_ij = w > 0, then there is an edge between node i and node j with weight w.
    #We will only consider undirected graphs, so A_ij = A_ji.
    #Therefore 'A' will be an upper right triangular matrix, with the diagonal being all zeros.
    #You can assume no edges have the same weight.
    #Output: 'T' is an NxN numpy array representing the minimum spanning tree of 'A'.
    #We will only consider undirected graphs, and therefore 'T' should be an upper right triangular matrix.

    def findMinimumSpanningTree(self,A):
        N = A.shape[0]
        u = self.makeUnionFind(N)
        T = numpy.zeros((N,N))
        edges = []
        for i in range(N):
            for j in range(i+1,N):
                if A[i][j] != 0:
                    edges.append([i,j,A[i][j]])
        edges = self.mergesort(edges)
        for i in range(len(edges)):
            s1 = self.find(u,edges[i][0])
            s2 = self.find(u,edges[i][1])
            if s1 != s2:
                u = self.union(u,s1,s2)
                T[edges[i][0]][edges[i][1]] = edges[i][2]
                T[edges[i][1]][edges[i][0]] = edges[i][2]
        return T

# Path: Project_1_Advanced_Algorithms\main.py


    