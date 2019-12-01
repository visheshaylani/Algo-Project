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
From = []
To = []
Cost = []
# Number of vertices in the graph 
V = no

# Define infinity as the large enough value. This value will be 
# used for vertices not connected to each other 
INF = 99999

# adjacency matrix
graph = [[INF for i in range(V)] for j in range(V)]
for i in range(len(node1)):
    graph[node1[i]][node2[i]] = cost[i]
#print(graph)
# Solves all pair shortest path via Floyd Warshall Algorithm 
def floydWarshall(graph, source): 
    dist = graph
    size = len(graph)
    path = [[0 for x in range(size)] for x in range (size)]
    for i in range(size):
        for j in range(size):
            if i == j:
                continue
            if dist[i][j] != INF and i != j:
                path[i][j] = i
            else:
                path[i][j] = -1
    for i in range(size):
        graph[i][i] = 0
                
    for k in range(V): 
        for i in range(V): 
            for j in range(V): 
                if dist[i][k] == INF or dist[k][j] == INF:
                    continue
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = round(dist[i][k] + dist[k][j] , 2)
                    path[i][j] = path[k][j]
# calculating edge
    for j in range(V):
        if j == source:
            continue
        temp = path[source][j]
        From.append(temp)
        To.append(j)

#    printSolution(dist)
#    displayPath(path, V)
#    printPath(path, V, source)
    
    return dist, path
# A utility function to print the solution 
def PrintPath(path, i, j):
    if path[i][j] == i:
        return
    PrintPath(path, i, path[i][j])
    
    print("%d →" %(path[i][j]), end = " ")
    
def printPath(path, V, source):
    print("Pair\t\tPath")
    for i in range(V):
#    i=source
        for j in range(V):
            if j != i and path[j][i] != 1:
#                print("Shortest Path from Vertex %d to vertex %d is ( %d" %(i,j,i) , end = " ")
                print("%d → %d\t\t(%d →" %(i,j,i), end = " ")
                PrintPath(path, i, j)
                print("%d)\n" %(j))
                      
def printSolution(dist): 
    print ("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(V): 
        for j in range(V): 
            if(dist[i][j] == INF): 
                print ("%.2f" %("INF")), 
            else: 
                print ("%.2f\t" %(dist[i][j]), end = " ") 
            if j == V-1: 
                print ("") 

def displayPath(path, V):
    print("")
    print ("Following matrix shows the shortest pair between every pair of vertices")
    for i in range(V):
        for j in range(V):
            print("%d\t" %(path[i][j]) , end = " ")
        print("")
    print("")
    
# Driver
def Floyd():
    return floydWarshall(graph, source); 

f = Floyd() # function calling
dist = f[0]
path = f[1]
#print(dist)
print("Node1: ", end = " ")
print(From)
print("Node2: ", end = " ")
print(To)
for i in range(len(From)):
    Cost.append(dist[From[i]][To[i]])
print("Bandwidth4: ", end = " ")
print(Cost)
#print("")
total=0.0
for i in range(V):
    total += dist[source][i]
graph_plot.PLOTTING(Node_Name, x, y, From, To, Cost, total)