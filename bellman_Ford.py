#from collections import defaultdict 
import File_Clean
import graph_plot

result = File_Clean.parse()
no = result[0]
node1 = result[1]
node2 = result[2]
cost = result[3]
source = result[4]
Node_Name = result[5]
x = result[6]
y = result[7]

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
        self.total_Distance = 0.0

    def addEdge(self, u, v, w): 
        self.graph.append([u, v, w]) 
        
    def printArr(self, source, dest, dist): 
        print("Vertex Distance from Source") 
        for i in range(self.V):
            print("% d \t\t %.2f" % (i, dist[i]))
            
        print("\n")
        print("Edge \t\t\tCost")
        for i in range(self.V):
            self.total_cost += adj[source[i]][dest[i]]
        for i in range(self.V):
            print(source[i], " - ", dest[i], "\t\t", round(adj[source[i]][dest[i]] , 4))
        for i in range(self.V):
            self.total_Distance = self.total_Distance + dist[i]
        print("")   
        print("Total Cost: ", round(self.total_cost , 4) )
        print("Total Distance: ", round(self.total_Distance , 4) )

    def BellmanFord(self, src): 
        dist = [float("Inf")] * self.V 
        dist[src] = 0
        dest = []
        source = []

        for i in range(self.V - 1): 
            for u, v, w in self.graph: 
                if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                        dist[v] = dist[u] + w 
                        source.append(u)
                        dest.append(v)
        for u, v, w in self.graph: 
                if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                        print ("Graph contains negative weight cycle")
                        return
 
        self.printArr(source, dest, dist)
        return source, dest, dist
#        print(source)
#        print(dest)
# driver
def Bellman():
    g = Graph(no)
    for i in range(len(node1)):
        g.addEdge(node1[i], node2[i], cost[i])

    return g.BellmanFord(source) 

b = Bellman()
From = []
To = []
Cost = []
dist = []

From = b[0]
To = b[1]
dist = b[2]
for i in range(len(From)):
    Cost.append(adj[From[i]][To[i]])
total = 0.0
for i in range(len(dist)):
    total = total + dist[i]
#print(total)
#print(From)
#print(To)
#print(Cost)
graph_plot.PLOTTING(Node_Name, x, y, From, To, Cost, total)