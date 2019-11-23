# Python program for Kruskal's algorithm to find 
# Minimum Spanning Tree of a given connected, 
# undirected and weighted graph 

from collections import defaultdict 
import File_Clean
import graph_plot
class Graph_: 

    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = [] # default dictionary 
                                # to store graph 
        

    # function to add an edge to graph 
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    # A utility function to find set of an element i 
    # (uses path compression technique) 
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    # A function that does union of two sets of x and y 
    # (uses union by rank) 
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 

        # Attach smaller rank tree under root of 
        # high rank tree (Union by Rank) 
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 

        # If ranks are same, then make one as root 
        # and increment its rank by one 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1

    # The main function to construct MST using Kruskal's 
        # algorithm 
    def KruskalMST(self): 

        result =[] #This will store the resultant MST 

        i = 0 # An index variable, used for sorted edges 
        e = 0 # An index variable, used for result[] 

            # Step 1: Sort all the edges in non-decreasing 
                # order of their 
                # weight. If we are not allowed to change the 
                # given graph, we can create a copy of graph 
        self.graph = sorted(self.graph,key=lambda item: item[2]) 

        parent = [] ; rank = [] 

        # Create V subsets with single elements 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
    
        # Number of edges to be taken is equal to V-1 
        while e < self.V -1 : 

            # Step 2: Pick the smallest edge and increment 
                    # the index for next iteration 
            u,v,w = self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 

            # If including this edge does't cause cycle, 
                        # include it in result and increment the index 
                        # of result for next edge 
            if x != y: 
                e = e + 1    
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             
            # Else discard the edge 

        # print the contents of result[] to display the built MST 
        print ("Following are the edges in the constructed MST")
        print("Egde \tWeight")
        total_cost= 0
        for u,v,weight in result: 
            #print str(u) + " -- " + str(v) + " == " + str(weight)
            total_cost += weight
            print ("%d -- %d == %.2f" % (u,v,weight))
        print("Total Cost: ", total_cost)
        return result
        
# Driver code  
def KRUSKAL():
    Result = File_Clean.parse()
    no = Result[0]
    node1 = Result[1]
    node2 = Result[2]
    cost = Result[3]
    source = Result[4]
    Node_Name = Result[5]
    x = Result[6]
    y = Result[7]
    
    
    g = Graph_(no)
    for i in range(len(node1)):
        g.addEdge(node1[i], node2[i], cost[i])
    
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
    
#print(From)
#print(To)
#print(cost)

graph_plot.PLOTTING(From, To, cost)
#This code is contributed by Neelam Yadav 
