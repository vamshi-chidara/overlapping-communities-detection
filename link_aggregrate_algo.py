import networkx as nx
import operator

# Calculate density of the community as metric
def community_weight(community):
    return float(2 * nx.number_of_edges(community) / nx.number_of_nodes(community))

# Order vertices based on rank in reverse order
def order_vertices_by_rank(graph):
    # Rank vertices based on the incoming links structure.
    vertices_rank = nx.pagerank(graph)
    ordered_vertices_map = map(lambda item: item[0],sorted(vertices_rank.items(), key = operator.itemgetter(1), reverse=True))
    ordered_vertices = list(ordered_vertices_map)
    return ordered_vertices

# Return list of communities which act as initial seeds to IS2 (Improved Interactive Scan) algorithm.
def link_aggregrate_algorithm(graph):
    communities=[]
    ordered_vertices = order_vertices_by_rank(graph)
    # Consider each vertex in the list of ordered vertices
    for vertex in ordered_vertices:
        added = False
        # Iterating over the current list of communities to find a community for this vertex.
        # We add this vertex to a community if the density of the community increases by adding this vertex.
        for i in range(len(communities)):
            C = communities[i]
            C_prime = C + [vertex]
            W_C = community_weight(graph.subgraph(C))
            W_C_prime = community_weight(graph.subgraph(C_prime))
            # Added vertex as density increased.
            if(W_C_prime>W_C):
                communities[i] = C_prime
                added = True
        # If vertex is not added to any community, we make the vertex as a new community.
        if(added == False):
            communities.append([vertex])
    return communities

