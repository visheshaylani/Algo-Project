import File_Clean

result = File_Clean.parse()
no = result[0]
node1 = result[1]
node2 = result[2]
cost = result[3]
source = result[4]
Node_Name = result[5]
x = result[6]
y = result[7]

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

G = {}
for i in range(len(node1)):
    make_link(G, node1[i], node2[i])
#print(G)
def clustering_coefficient(G,v):
    neighbors = G[v].keys()
    if len(neighbors) == 1: 
        return -1.0
    links = 0
    for w in neighbors:
        for u in neighbors:
            if u in G[w]: 
                links += 0.5 #0.5
#    print("links: %.2f" %(links))
#    print("neighbor: %.2f" %(len(neighbors)))
    return 2.0*links/(len(neighbors)*(len(neighbors)-1))

#print ("For 3: ",round(clustering_coefficient(G,8) , 4), " ", end = " ")

print("Local Clusttering Coefficient of every vertex: ")
#for i in range(no):
for i in G.keys():
    print (round(clustering_coefficient(G,i) , 4), " ", end = " ")  #ORD
#    print(i, " ", end = " ")
print("")
print("")
total = 0
for v in G.keys():
##    print(round(clustering_coefficient(G,v) ,4))
##    print("")
    total += clustering_coefficient(G,v)
##print(total)
print("Average: ", end = " ")
print (round(total/len(G) , 3))