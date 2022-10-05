import networkx as nx

def community_weight(community):
	return float(2 * nx.number_of_edges(community) / nx.number_of_nodes(community))


def improved_iterative_scan_algo(community,graph):
	community_graph = graph.subgraph(community)
	W = community_weight(community_graph)
	metric_increase = True
	while metric_increase:
		N = list(community_graph.nodes)
		for vertex in community_graph.nodes:
			adjacent_nodes = set(graph.neighbors(vertex))
			N_with_adjacent_nodes = set(N).union(adjacent_nodes)
			N = list(N_with_adjacent_nodes)
		for vertex in N:
			vertices = list(community_graph.nodes)
			if vertex in vertices:
				vertices.remove(vertex)
			else:
				vertices.append(vertex)
			if not vertices:
				W_prime=0
			else:
				community_graph_prime = graph.subgraph(vertex)
				W_prime = community_weight(community_graph_prime)
			# cur_w = float(2 * nx.number_of_edges(cur) / nx.number_of_nodes(cur))
			if W_prime > W:
				community_graph = community_graph_prime.copy()
		W_new = community_weight(community_graph)
		if W_new == W:
			increase = False
		else:
			W = W_new
	return list(community_weight.nodes)