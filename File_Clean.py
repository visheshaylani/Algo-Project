import networkx as nx
import matplotlib.pyplot as plt

def parse():
    f = open('input10.txt', 'r')
    # deleting initial two lines
    f.readline()
    f.readline()
    # taking an total nodes of nodes as input
    num = f.readline()
    # converting str to int
    num = int(num) 
    # deleting line 3
    f.readline()
    
    # initializing arrays
    nodes=[]
    x_cordinate=[]
    y_cordinate=[]
    Node_1=[]
    Node_2=[]
    Bandwidth=[]

    for i in range(num):
        content = f.readline()
        x, y, z = content.split('\t')
        x = int(x)
        y = float(y)
        z = float(z)
        
        nodes.append(x)
        x_cordinate.append(y)
        y_cordinate.append(z)

    # deleting a lines before edges
    f.readline()
    n=int(0)
    # edges 
    for i in range(num):
        content = f.readline()
        data = content.split()
        for j in range(0, len(data)-1, 4):
            Node_1.append(n)
            temp = int(data[j+1])
            Node_2.append(temp)
            temp1 = float(data[j+3])
            Bandwidth.append(temp1/10000000)
        n = n+1
    # deleting a empty second last line 
    f.readline()
    source = f.readline()
    source = int(source)
#    print(nodes)
#    print(x_cordinate)
#    print(y_cordinate)
#    print(Node_1)
#    print(Node_2)
#    print(Bandwidth)
#    print(source)
#    closing file.
    f.close()
#    G = nx.Graph()
#    for i in range(len(nodes)):
#        G.add_node(nodes[i], pos=(x_cordinate[i], y_cordinate[i]))
#    mat = [[0 for i in range(len(Node_1))] for j in range(len(Node_2))]
#    for i in range(len(Node_1)):
#        mat[i] = u,v,w = Node_1[i], Node_2[i], Bandwidth[i]
#    #print (mat)
#    for i in range(len(Node_1)):
#        G.add_weighted_edges_from(mat)
#    print("Actual Graph: ")
#    nx.draw(G, nx.get_node_attributes(G, 'pos'), with_labels=True, node_size=400)
    return num, Node_1, Node_2, Bandwidth, source, nodes, x_cordinate, y_cordinate
    
# driver
#parse()