import sys 
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
        
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)] 
                    for row in range(vertices)] 
        self.total_cost = 0.0
        self.total_Distance = 0.0
        
    def printSolution(self, source, dest, dist): 
        print ("Vertex \tDistance from Source")
        for node in range(self.V):
            print (node, "\t", round(dist[node] , 4))
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
        print("Tota Distance: ", round(self.total_Distance , 4) )

    def minDistance(self, dist, sptSet): 

        min = sys.maxsize

        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 

        return min_index 

    def dijkstra(self, src): 

        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
        dest = []
        source = []
        for cout in range(self.V): 
            u = self.minDistance(dist, sptSet) 
            sptSet[u] = True
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
    g = Graph(no)  
    g.graph = adj
    
    return g.dijkstra(source) 

d = Dijkstra()
From = []
To = []
Cost = []
dist = []

From = d[0]
To = d[1]
dist = d[2]
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