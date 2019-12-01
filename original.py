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

total = 0.0
for i in range(len(cost)):
    total = total + cost[i]
#print(round(total, 4))
    
graph_plot.PLOTTING(Node_Name, x, y, node1, node2, cost, total)