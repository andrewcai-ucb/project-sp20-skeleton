import networkx as nx
from parse import read_input_file, write_output_file, read_output_file
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
    
    def dijkstra_tree(r):
 
        T = nx.Graph()
        T.add_nodes_from(G)
        for p in nx.single_source_dijkstra_path(G, r).values():
            nx.add_path(T, p)
        return T
        
    
    def pruned_tree(T):  
        """Removes edges from a spanning tree to obtain a dominating tree.

        Args:
            r: Root

        """    
        for (u, v) in T.edges():
            T[u][v]['weight'] = G[u][v]['weight']
            
        opt_cost = average_pairwise_distance_fast(T.to_undirected())
        
        leaves = PriorityQueue()
        for l in T:
            if T.degree(l) == 1:
                leaves.put((-G[l][list(T[l])[0]]['weight'], l))
                
        while not leaves.empty():
            v = leaves.get()[1]
            if T.degree(v) == 1:
                w = list(T[v])[0]
                T.remove_node(v)
                if not is_valid_network(G, T):
                    T.add_edge(v, w, weight=G[v][w]['weight'])
                else:
                    c = average_pairwise_distance_fast(T)
                    if c < opt_cost:
                        opt_cost = c
                        if T.degree(w) == 1:
                            leaves.put((-G[w][list(T[w])[0]]['weight'], w))
                    else: 
                        T.add_edge(v, w, weight=G[v][w]['weight'])      
        
        for l in T:
            if T.degree(l) == 1:
                leaves.put((-G[l][list(T[l])[0]]['weight'], l))
                
        while not leaves.empty():
            v = leaves.get()[1]
            if T.degree(v) == 1:
                w = list(T[v])[0]
                T.remove_node(v)
                if not is_valid_network(G, T):
                    T.add_edge(v, w, weight=G[v][w]['weight'])
                else:
                    c = average_pairwise_distance_fast(T)
                    if c < opt_cost:
                        opt_cost = c
                        if T.degree(w) == 1:
                            leaves.put((-G[w][list(T[w])[0]]['weight'], w))
                    else: 
                        T.add_edge(v, w, weight=G[v][w]['weight'])      
                
        return T
    
    return min([pruned_tree(dijkstra_tree(v)) for v in G] + 
        [pruned_tree(nx.bfs_tree(G, v).to_undirected()) for v in G] + 
        [pruned_tree(nx.minimum_spanning_tree(G)) for v in G], key=average_pairwise_distance_fast)
        
# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

if __name__ == '__main__':
    assert len(sys.argv) == 2
    path = sys.argv[1]
    G = read_input_file(path)
    T = solve(G)
    assert is_valid_network(G, T)
    print("Average  pairwise distance: {}".format(average_pairwise_distance_fast(T)))
    write_output_file(T, 'test.out')
    
