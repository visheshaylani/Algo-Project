import networkx as nx
import matplotlib.pyplot as plt

#G = nx.DiGraph()
def PLOTTING(Node_Name, x, y, From, To, weight, total_cost):
    G = nx.DiGraph()

    for i in range(len(Node_Name)):
        G.add_node(Node_Name[i], pos=(x[i], y[i]))
        
    for i in range(len(From)):
        G.add_edge(From[i], To[i], weight=weight[i])

    pos = nx.get_node_attributes(G, 'pos')

    fig, ax = plt.subplots()
    nx.draw_networkx(G, nx.get_node_attributes(G, 'pos'), with_labels=True, node_size=400, ax = ax)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels = labels)
    
#    ax.draw_networkx_nodes(..., ax=ax)
    ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()

    plt.xlabel("Total Cost: %.2f" %(total_cost))
    plt.show()