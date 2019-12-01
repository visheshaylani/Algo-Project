import File_Clean
import graph_plot

Result = File_Clean.parse()
no = Result[0]
node1 = Result[1]
node2 = Result[2]
cost = Result[3]
source = Result[4]
Node_Name = Result[5]
x = Result[6]
y = Result[7]
    
class Graph_: 

    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = [] # default dictionary to store graph 
        
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 

        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
            
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 

        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1

    def KruskalMST(self): 

        result =[] #This will store the resultant MST 

        i = 0 # An index variable, used for sorted edges 
        e = 0 # An index variable, used for result[] 

        self.graph = sorted(self.graph,key=lambda item: item[2]) 

        parent = [] ; rank = [] 

        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
    
        # Number of edges to be taken is equal to V-1 
        while e < self.V -1 : 
            u,v,w = self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 

            if x != y: 
                e = e + 1    
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             
            # Else discard the edge 

        # print the contents of result[] to display the built MST 
        
        print ("Following are the edges in the constructed MST")
        print("Egde \t\tWeight")
        total_cost= 0
        for u,v,weight in result: 
            total_cost += weight
            print ("%d-%d \t\t %.2f" % (u,v,weight))
        print("")
        print("Total Cost: ", round(total_cost , 4))
        return result
        
# Driver code 
g = Graph_(no)
for i in range(len(node1)):
    g.addEdge(node1[i], node2[i], cost[i])  
    
def KRUSKAL():
    return g.KruskalMST() 

From = []
To = []
cost = []
k = KRUSKAL()   # function calling
#print(k)
for u,v,w in k:
    From.append(u)
    To.append(v)
    cost.append(w)
total = 0.0
for i in range(len(cost)):
    total = total + cost[i]
#print(From)
#print(To)
#print(cost)

graph_plot.PLOTTING(Node_Name, x, y, From, To, cost, total)
