# A Python program for Prim's Minimum Spanning Tree (MST) algorithm. 
# The program is for adjacency matrix representation of the graph 

import sys # Library for INT_MAX
import File_Clean
import graph_plot
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)] 
                    for row in range(vertices)] 

    # A utility function to print the constructed MST stored in parent[] 
    def printMST(self, parent):
        F = []
        T = []
        C = []
        total_cost = 0
        for i in range(self.V):
            total_cost += self.graph[i][ parent[i] ]
        print ("Edge \tWeight")
        for i in range(1, self.V): 
            print (parent[i], "-", i, "\t", self.graph[i][ parent[i] ] )
            F.append(parent[i])
            T.append(i)
            C.append(self.graph[i][parent[i]])
            
        print ("Total Cost: ", round(total_cost , 4))
#        print(F)
#        print(T)
#        print(C)
        return F,T,C
        
    # A utility function to find the vertex with 
    # minimum distance value, from the set of vertices 
    # not yet included in shortest path tree 
    def minKey(self, key, mstSet): 

        # Initilaize min value 
        min = sys.maxsize

        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 

        return min_index 

    # Function to construct and print MST for a graph 
    # represented using adjacency matrix representation 
    def primMST(self, source): 

        # Key values used to pick minimum weight edge in cut 
        key = [sys.maxsize] * self.V 
        parent = [None] * self.V # Array to store constructed MST 
        # Make key 0 so that this vertex is picked as first vertex 
        key[0] = source
        mstSet = [False] * self.V 

        parent[0] = -1 # First node is always the root of 

        for cout in range(self.V): 

            # Pick the minimum distance vertex from 
            # the set of vertices not yet processed. 
            # u is always equal to src in first iteration 
            u = self.minKey(key, mstSet) 

            # Put the minimum distance vertex in 
            # the shortest path tree 
            mstSet[u] = True

            # Update dist value of the adjacent vertices 
            # of the picked vertex only if the current 
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                # graph[u][v] is non zero only for adjacent vertices of m 
                # mstSet[v] is false for vertices not yet included in MST 
                # Update the key only if graph[u][v] is smaller than key[v] 
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        parent[v] = u 

        Result = self.printMST(parent) 
#        print(Result)
        return Result
            
# driver
def PRIMS():
    result = File_Clean.parse()
    no = result[0]
    node1 = result[1]
    node2 = result[2]
    cost = result[3]
    source = result[4]
    # initailizing an array adj and declare with zero
    adj = [[0 for i in range(no)] for y in range(no)]
    # calculating adjacency matrix
    for i in range(len(node1)):
        adj[node1[i]][node2[i]] = cost[i]
    
    g = Graph(no) 
    g.graph = adj
    
    return g.primMST(source); 

From = []
To = []
cost = []    
p = PRIMS()
#print(p)
From = p[0]
To = p[1]
cost = p[2]

#print(From)
#print(To)
#print(cost)
graph_plot.PLOTTING(From, To, cost)
# Contributed by Divyanshu Mehta 
