import File_Clean
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#G = nx.DiGraph()
def PLOTTING(From, To, weight):
    G = nx.DiGraph()
    result = File_Clean.parse()
    Node_Name = result[5]
    x = result[6]
    y = result[7]

    for i in range(len(Node_Name)):
        G.add_node(Node_Name[i], pos=(x[i], y[i]))
        
#    mat = [[0 for i in range(len(From))] for j in range(len(To))]
#    for i in range(len(From)):
#            mat[i] = u,v,w = From[i], To[i], float(weight[i])
    #print (mat)
    for i in range(len(From)):
#        G.add_weighted_edges_from(mat)
        G.add_edge(From[i], To[i], weight=weight[i])

    pos = nx.get_node_attributes(G, 'pos')
    #nx.draw_networkx_nodes(G, nx.get_node_attributes(G, 'pos'), node_size=400)
    #nx.draw_networkx_edges(G, 'pos', with_labels=True, node_size=400)
#    ax.plot(x, y)
#    ax.set_title('A single plot')
#    fig, ax = plt.subplots()
    
    nx.draw(G, nx.get_node_attributes(G, 'pos'), with_labels=True, node_size=400)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels = labels)
    
#    ax.draw_networkx_nodes(..., ax=ax)
#    ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    plt.show()
#PLOTTING()