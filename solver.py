import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_network, average_pairwise_distance, average_pairwise_distance_fast
import sys

import os.path
from queue import PriorityQueue


def solve(G):
    """
    Args:
        G: networkx.Graph

    Returns:
        T: networkx.Graph
    """

    M = nx.minimum_spanning_tree(G)
    
    def min_routing_cost_tree(r):
 
        T = nx.DiGraph()
        T.add_nodes_from(G)
        for p in nx.single_source_dijkstra_path(G, r).values():
            nx.add_path(T, p)
        for (u, v) in T.edges():
            T[u][v]['weight'] = G[u][v]['weight']
        
        return T
        
    def weighted_bfs_tree(r):
 
        T = nx.bfs_tree(G, r)
        for (u, v) in T.edges():
            T[u][v]['weight'] = G[u][v]['weight']
        
        return T
        
    def weighted_mst_tree(r):
 
        T = nx.bfs_tree(M, r)
        for (u, v) in T.edges():
            T[u][v]['weight'] = G[u][v]['weight']
        
        return T
    
    def pruned_tree(T):  
        """Removes edges from a spanning tree to obtain a dominating tree.

        Args:
            r: Root

        """    
        opt_cost = average_pairwise_distance_fast(T.to_undirected())
        
        leaves = PriorityQueue()
        for l in T:
            if ((T.in_degree(l) == 1) and (T.out_degree(l) == 0)):
                leaves.put(l, -G[l][list(T.pred[l])[0]]['weight'])
                
        while not leaves.empty():
            v = leaves.get()
            S = T.to_undirected()
            S.remove_node(v)
            c = average_pairwise_distance_fast(S)
            if ((c < opt_cost) and is_valid_network(G, S)):
                opt_cost = c
                if T.in_degree(v) == 1:
                    w = T.pred[v];
                    if T.in_degree(w) == 1:
                        leaves.put(w, -G[w][T.pred[l].keys[0]]['weight'])
                T.remove_node(v)  
                
        return T.to_undirected()
    
    return min([pruned_tree(min_routing_cost_tree(v)) for v in G] + 
        [pruned_tree(weighted_bfs_tree(v)) for v in G] + 
        [pruned_tree(weighted_mst_tree(v)) for v in G], key=average_pairwise_distance_fast)

# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

if __name__ == '__main__':
    assert len(sys.argv) == 2
    path = sys.argv[1]
    G = read_input_file(path)
    T = solve(G)
    assert is_valid_network(G, T)
    print("Average  pairwise distance: {}".format(average_pairwise_distance(T)))
    write_output_file(T, 'test.out')
    
