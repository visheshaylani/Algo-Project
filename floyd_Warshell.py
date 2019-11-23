from math import inf
from itertools import product
import File_Clean

def floyd_warshall(n, edge):
    rn = range(n)
    dist = [[inf] * n for i in rn]
    nxt = [[0] * n for i in rn]
    for i in rn:
        dist[i][i] = 0
    for u, v, w in edge:
        dist[u - 1][v - 1] = w
        nxt[u - 1][v - 1] = v - 1
    for k, i, j in product(rn, repeat=3):
        sum_ik_kj = dist[i][k] + dist[k][j]
        if dist[i][j] > sum_ik_kj:
            dist[i][j] = sum_ik_kj
            nxt[i][j] = nxt[i][k]
    print("    pair        dist     path")
    for i, j in product(rn, repeat=2):
        if i != j:
            path = [i]
            while path[-1] != j:
                path.append(nxt[path[-1]][j])
            print("%3d → %3d  %4d       %s"
                  % (i + 1, j + 1, dist[i][j],
                     ' → '.join(str(p + 1) for p in path)))


if __name__ == '__main__':
    result = File_Clean.parse()
    no = result[0]
    node1 = result[1]
    node2 = result[2]
    cost = result[3]
    source = result[4]
    edge = node1
    u = []
    v = []
    w = []
#    for i in node1:
#        u.append(i)
#    for i in node2:
#        v.append(i)
#    for i in cost:
#        w.append(i)
#    mat = [[0 for i in range(no)] for j in range(no)]
#    for i in range(no):
#        for j in range(no):
#            mat[i][j] = a, b, c = u[i], v[i], w[i]
#    
#    a = []
#    for i in mat:
#        for j in i:
#            a.append(list(j))
#    
#    print(a)
#    print(len(a))
    floyd_warshall(4, [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]])
#    floyd_warshall(4, [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]])
#    floyd_warshall(no, a)
