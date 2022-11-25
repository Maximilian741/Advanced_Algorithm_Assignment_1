#Max Casteel
#Programming Assignment 1 - Uninon find adjacency matrix to find MST using Kruskals algorithm.
#Advanced Algorithms

import numpy as np
import numpy
import kruskalClass
 #import numpy for matrix operations
class kruskalClass:
    def __init__(self):
        #Just a quit test to see if the object was created correctly.
        print("kruskalClass object created")    

    #s = find(u,v)
    #Input: 'u' is a union-find structure.  'v' is a numerical index of a graph node.
    #Output: 's' is the muerical value corresponding to the label for the set of connected nodes to which 'v' belongs.
    def find(self,u,v):
        #if the node is the root of the tree, then return the node.
        if u[v][0] == v:
            return v
            #if the node is not the root of the tree, then recursively call the find function on the parent node.
        else:
            return self.find(u,u[v][0])

    #u_out = union(u_in,s1,s2)
    #Input: 'u_in' is a union-find data structure. 's1' and 's2' are numerical values
    #corresponding to the labels of two groups of graph nodes.
    #Output: 'u_out' is a union-find data structure that is the result of merging the two sets of nodes.
    def union(self,u_in,s1,s2):
        #checks to see if the two sets are already in the same connected component.
        if self.find(u_in,s1) == self.find(u_in,s2):
            return u_in
        #if the two sets are not in the same connected component, then merge the two sets.
        else:
            #if the size of the first set is greater than the size of the second set, then merge the second set into the first set.
            if u_in[s1][1] > u_in[s2][1]:
                #u_in[s2][0] = u_in[s1][0]
                u_in[s2][0] = s1
                #This is adding the total weight from the previous connected component to the new connected component.
                u_in[s1][1] += u_in[s2][1]
                return u_in
            #if the size of the second set is greater than the size of the first set, then merge the first set into the second set.
            else:
                #u_in[s1][0] = u_in[s2][0]
                u_in[s1][0] = s2
                u_in[s2][1] += u_in[s1][1]
                return u_in

    #u = makeUnionFind(N)
    #Input: 'N' is the number of nodes in a graph.
    #Output: 'u' is a 1xN python dictionary, where the keys are numerical labels
    #for the nodes, and the values are numpy arrays with the 0th entry being a pointer 
    #to a node in the same dictionary.  The numpy arrays can be more than one 1-D if you want, but they must be numpy
    #arrays, and the 0th entry must contain pointers to other nodes that are used
    #in the 'find' and 'union' functions.
    def makeUnionFind(self,N):  
        #u is a 1xN pytohn dictionary
        u = {}
        #for loop to create an 1xN numpy array for each node in the graph.
        for i in range(N):
            #u[i] is a 1xN numpy array
            u[i] = np.array([i,1])
        return u
       

    #b = mergesort(a)
    #Input: 'a' is a 1xK numpy array.
    #Output: 'b' is a 1xK numpy array with elements in ascending order. (ie. b[0] <= b[1] <= ... <= b[K-1] ==> lowest value to highest value)
    def mergesort(self,a):
        #Decided to just return 'a' as if it were equivalent to 'b' because the list of edges is already sorted. As seen below
        if len(a) > 1:
            #split the array into two halves
            mid = len(a)//2
            left = a[:mid]
            right = a[mid:]
            #recursively call mergesort on the left and right halves of the array.
            self.mergesort(left)
            self.mergesort(right)
            #intialize index variables.
            i = 0
            j = 0
            k = 0
            #while loop to sort the array.
            while i < len(left) and j < len(right):
                #if the weight of the LEFT edge is less than the weight of the right edge, then add the left edge to the sorted array.
                if left[i][2] < right[j][2]:
                    a[k] = left[i]
                    i += 1
                #if the weight of the RIGHT edge is less than the weight of the left edge, then add the right edge to the sorted array.
                else:
                    a[k] = right[j]
                    j += 1
                k += 1
            #Houskeeping to check if any elements weer left over
            #if there are elements left over in the LEFT array, then add them to the sorted array.
            while i < len(left):
                a[k] = left[i]
                i += 1
                k += 1
                #if there are elements left over in the RIGHT array, then add them to the sorted array.
            while j < len(right):
                a[k] = right[j]
                j += 1
                k += 1
        #return the sorted array. a == b per the instructions.
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
        #N is the number of nodes in the graph.
        #u is the union-find data structure.
        #T is the minimum spanning tree.
        N = A.shape[0]
        u = self.makeUnionFind(N)
        #create a list initialized to all zeros.
        T = numpy.zeros((N,N))
        edges = []
        #iterate through the adjacency matrix to find all the edges in the graph.
        for i in range(N):
            for j in range(i+1,N):
                #if the weight of the edge is greater than zero, then add the edge to the list of edges.
                if A[i][j] != 0:
                    edges.append([i,j,A[i][j]])
        #sort the list of edges.
        edges = self.mergesort(edges)
        #iterate through the list of edges.
        for i in range(len(edges)):
            #if the two nodes that the edge connects are not in the same connected component, then add the edge to the minimum spanning tree.
            s1 = self.find(u,edges[i][0])
            s2 = self.find(u,edges[i][1])
            #if the two nodes that the edge connects are not in the same connected component, then add the edge to the minimum spanning tree.
            if s1 != s2:
                #add the edge to the minimum spanning tree.
                u = self.union(u,s1,s2)
                T[edges[i][0]][edges[i][1]] = edges[i][2]
        return T

