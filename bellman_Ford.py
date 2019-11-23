# Python program for Bellman-Ford's single source 
# shortest path algorithm. 

from collections import defaultdict 
import File_Clean
import graph_plot

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
        
# Class to represent a graph 
class Graph: 

    def __init__(self, vertices): 
        self.V = vertices # No. of vertices 
        self.graph = [] # default dictionary to store graph 
        self.total_cost = 0.0
        
    # function to add an edge to graph 
    def addEdge(self, u, v, w): 
        self.graph.append([u, v, w]) 
        
    # utility function used to print the solution 
    def printArr(self, source, dest, dist): 
        print("Vertex Distance from Source") 
        for i in range(self.V):
            print("% d \t\t %.2f" % (i, dist[i]))
            
        print("\n")
        print("Edge \t\tCost")
        for i in range(self.V):
            self.total_cost += adj[source[i]][dest[i]]
        for i in range(self.V):
            print(source[i], " - ", dest[i], "\t", round(adj[source[i]][dest[i]] , 4))

        print("Total Cost: ", round(self.total_cost , 4) )
    # The main function that finds shortest distances from src to 
    # all other vertices using Bellman-Ford algorithm. The function 
    # also detects negative weight cycle 
    def BellmanFord(self, src): 

        # Step 1: Initialize distances from src to all other vertices 
        # as INFINITE 
        dist = [float("Inf")] * self.V 
        dist[src] = 0
        dest = []
        source = []

        # Step 2: Relax all edges |V| - 1 times. A simple shortest 
        # path from src to any other vertex can have at-most |V| - 1 
        # edges 
        for i in range(self.V - 1): 
            # Update dist value and parent index of the adjacent vertices of 
            # the picked vertex. Consider only those vertices which are still in 
            # queue 
            for u, v, w in self.graph: 
                if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                        dist[v] = dist[u] + w 
                        source.append(u)
                        dest.append(v)
        # Step 3: check for negative-weight cycles. The above step 
        # guarantees shortest distances if graph doesn't contain 
        # negative weight cycle. If we get a shorter path, then there 
        # is a cycle. 

        for u, v, w in self.graph: 
                if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                        print ("Graph contains negative weight cycle")
                        return
                        
        # print all distance 
        self.printArr(source, dest, dist)
        return source, dest, dist
#        print(source)
#        print(dest)
# driver
def Bellman():
#    result = File_Clean.parse()
#    no = result[0]
#    node1 = result[1]
#    node2 = result[2]
#    cost = result[3]
#    source = result[4]
#    
    g = Graph(no)
    for i in range(len(node1)):
        g.addEdge(node1[i], node2[i], cost[i])
    
    # Print the solution 
    return g.BellmanFord(source) 

b = Bellman()
From = []
To = []
Cost = []

From = b[0]
To = b[1]
for i in range(len(From)):
    Cost.append(adj[From[i]][To[i]])
#print(From)
#print(To)
#print(Cost)
graph_plot.PLOTTING(From, To, Cost)
# This code is contributed by Neelam Yadav 
