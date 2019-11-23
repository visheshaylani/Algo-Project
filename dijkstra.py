# Python program for Dijkstra's single 
# source shortest path algorithm. The program is 
# for adjacency matrix representation of the graph 

# Library for INT_MAX 
import sys 
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
        
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)] 
                    for row in range(vertices)] 
        self.total_cost = 0.0
        
    def printSolution(self, source, dest, dist): 
#        print(dest)
        print ("Vertex \tDistance from Source")
        for node in range(self.V):
            print (node, "\t", round(dist[node] , 4))
        print("\n")
        print("Edge \t\tCost")
        for i in range(self.V):
            self.total_cost += adj[source[i]][dest[i]]
        for i in range(self.V):
            print(source[i], " - ", dest[i], "\t", round(adj[source[i]][dest[i]] , 4))

        print("Total Cost: ", round(self.total_cost , 4) )
        
    # A utility function to find the vertex with 
    # minimum distance value, from the set of vertices 
    # not yet included in shortest path tree 
    def minDistance(self, dist, sptSet): 

        # Initilaize minimum distance for next node 
        min = sys.maxsize

        # Search not nearest vertex not in the 
        # shortest path tree 
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 

        return min_index 

    # Funtion that implements Dijkstra's single source 
    # shortest path algorithm for a graph represented 
    # using adjacency matrix representation 
    def dijkstra(self, src): 

        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
        dest = []
        source = []
        for cout in range(self.V): 

            # Pick the minimum distance vertex from 
            # the set of vertices not yet processed. 
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, sptSet) 
#            dest.append(u)
            # Put the minimum distance vertex in the 
            # shotest path tree 
            sptSet[u] = True

            # Update dist value of the adjacent vertices 
            # of the picked vertex only if the current 
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v] 
                        source.append(u)
                        dest.append(v)
#        print(source)
#        print(dest)
        self.printSolution(source, dest, dist)
        return source, dest, dist
# Driver program 
def Dijkstra():
#    result = File_Clean.parse()
#    no = result[0]
#    node1 = result[1]
#    node2 = result[2]
#    cost = result[3]
#    source = result[4]
#    # initailizing an array adj and declare with zero
#    adj = [[0 for i in range(no)] for y in range(no)]
#    # calculating adjacency matrix
#    for i in range(len(node1)):
#        adj[node1[i]][node2[i]] = cost[i]
    
    g = Graph(no)  
    g.graph = adj
    
    return g.dijkstra(source) 
d = Dijkstra()
From = []
To = []
Cost = []
#adj = []

From = d[0]
To = d[1]
for i in range(len(From)):
    Cost.append(adj[From[i]][To[i]])

#
#print(From)
#print(To)
#print(Cost)
graph_plot.PLOTTING(From, To, Cost)
# This code is contributed by Divyanshu Mehta 
