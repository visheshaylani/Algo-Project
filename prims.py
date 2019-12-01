import sys # Library for INT_MAX
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

    def printMST(self, parent):
        F = []
        T = []
        C = []
        total_cost = 0
        for i in range(self.V):
            total_cost += self.graph[i][ parent[i] ]
        print ("Edge \t\t\tWeight")
        for i in range(1, self.V): 
            print ("%d-%d \t\t\t %.2f" % (parent[i], i, self.graph[i][parent[i]]))
            F.append(parent[i])
            T.append(i)
            C.append(self.graph[i][parent[i]])
        print("")   
        print ("Total Cost: ", round(total_cost , 4))
#        print(F)
#        print(T)
#        print(C)
        return F, T, C, total_cost
        
    def minKey(self, key, mstSet): 

        # Initilaize min value 
        min = sys.maxsize

        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 

        return min_index 

    def primMST(self, source): 
        key = [sys.maxsize] * self.V 
        parent = [None] * self.V # Array to store constructed MST 
        # Make key 0 so that this vertex is picked as first vertex 
        key[0] = source
        mstSet = [False] * self.V 

        parent[0] = -1 # First node is always the root of 

        for cout in range(self.V): 
            u = self.minKey(key, mstSet) 
 
            mstSet[u] = True

            for v in range(self.V): 
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        parent[v] = u 

        Result = self.printMST(parent) 
#        print(Result)
        return Result
            
# driver
def PRIMS():
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
total = 0.0
for i in range(len(cost)):
    total = total + cost[i]
#print(total)
#print(From)
#print(To)
#print(cost)
graph_plot.PLOTTING(Node_Name, x, y, From, To, cost, total)