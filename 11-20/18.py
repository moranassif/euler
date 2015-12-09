__author__ = 'Moran'

import networkx
import matplotlib.pyplot as plt

triag = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

lines = triag.splitlines()
lines = [line.split() for line in lines]


def dag_longest_path(G, weight='weight', default_weight=1):
    """Returns the longest path in a DAG
    If G has edges with 'weight' attribute the edge data are used as weight values.

    Parameters
    ----------
    G : NetworkX DiGraph
        Graph

    weight : string (default 'weight')
        Edge data key to use for weight

    default_weight : integer (default 1)
        The weight of edges that do not have a weight attribute

    Returns
    -------
    path : list
        Longest path

    Raises
    ------
    NetworkXNotImplemented
        If G is not directed

    See also
    --------
    dag_longest_path_length
    """
    dist = {} # stores {v : (length, u)}
    for v in networkx.topological_sort(G):
        us = [(dist[u][0] + data.get(weight, default_weight), u)
            for u, data in G.pred[v].items()]
        # Use the best predecessor if there is one and its distance is non-negative, otherwise terminate.
        maxu = max(us) if us else (0, v)
        dist[v] = maxu if maxu[0] >= 0 else (0, v)
    u = None
    v = max(dist, key=dist.get)
    path = []
    while u != v:
        path.append(v)
        u = v
        v = dist[v][1]
    path.reverse()
    return path



def dag_longest_path_length(G):
    """Returns the longest path length in a DAG

    Parameters
    ----------
    G : NetworkX DiGraph
        Graph

    Returns
    -------
    path_length : int
        Longest path length

    Raises
    ------
    NetworkXNotImplemented
        If G is not directed

    See also
    --------
    dag_longest_path
    """
    path_length = len(networkx.dag_longest_path(G)) - 1
    return path_length

g = networkx.DiGraph()
# Build the graph
line_num = 1
g.add_node((0, 0))
prev_line = lines[0]
for line in lines[1:]:
    print("line is {}".format(line))
    for i in range(len(prev_line)):
        print("i is {}".format(i))
        g.add_edge((line_num-1, i), (line_num, i), weight=int(line[i]))
        print("Adding from {} to {} with weight {}".format((line_num-1, i), (line_num, i), 1/int(line[i])))
        g.add_edge((line_num-1, i), (line_num, i+1), weight=int(line[i+1]))
        print("Adding from {} to {} with weight {}".format((line_num-1, i), (line_num, i+1), 1/int(line[i+1])))
    line_num += 1
    prev_line = line
# Add collection node
g.add_node((-1, -1))
for i in range(len(prev_line)):
    g.add_edge((line_num-1, i), (-1, -1), weight=1)

#networkx.draw_networkx(g, with_labels=True)
#plt.show()

# Find the shortest path
path = dag_longest_path(g, weight="weight")
sum = 0
for (line_num, elem_num) in path[:-1]:
    print("adding {}".format(lines[line_num][elem_num]))
    sum += int(lines[line_num][elem_num])

# Subtract the last one
print(path)
print(sum)

