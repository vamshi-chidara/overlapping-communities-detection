import networkx as nx
import operator

def community_weight(community):
    return float(2 * nx.number_of_edges(community) / nx.number_of_nodes(community))

def order_vertices_by_rank(graph):
    vertices_rank = nx.pagerank(graph)
    ordered_vertices_map = map(lambda item: item[0],sorted(vertices_rank.items(), key = operator.itemgetter(1), reverse=True))
    ordered_vertices = list(ordered_vertices_map)
    print(ordered_vertices)
    return ordered_vertices

def link_aggregrate_algorithm(graph):
    communities=[]
    ordered_vertices = order_vertices_by_rank(graph)

    for vertex in ordered_vertices:
        added = False
        for i in range(len(communities)):
            C = communities[i]
            C_prime = C + [vertex]
            W_C = community_weight(graph.subgraph(C))
            W_C_prime = community_weight(graph.subgraph(C_prime))
            if(W_C_prime>W_C):
                communities[i] = C_prime
                added = True
        if(added == False):
            communities.append([vertex])
    return communities

