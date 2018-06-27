import networkx as nx

# This function takes as input a graph g.
# The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
# undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
# and has no self-loops (i.e., there are no edges from i to i).
#
# The function should return a 2-approximation of an optimal Hamiltonian cycle.

def approximation(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    # You might want to use the function "nx.minimum_spanning_tree(g)"
    # which returns a Minimum Spanning Tree of the graph g

    # You also might want to use the command "list(nx.dfs_preorder_nodes(graph, 0))"
    # which gives a list of vertices of the given graph in depth-first preorder.

    # 1. find the MST of the graph
    mstG = nx.minimum_spanning_tree(g);
    # 2. double the edges of the MST
    # 3. find the eulerian cycle from the doubled MST graph
    # 4. follow the eulerian cycle, bypass duplicated nodes 
    sub_cycle = list(nx.dfs_preorder_nodes(mstG, 0));
    # 5. connect the final and the first nodes 
    weight = sum([g[sub_cycle[i]][sub_cycle[i + 1]]['weight'] for i in range(len(sub_cycle) - 1)])
	weight = weight + g[sub_cycle[-1]][sub_cycle[0]]['weight']

    return weight


    