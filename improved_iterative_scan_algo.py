'''
Improved Iterative Scan Algorithm: 
Improved Iterative Scan Algorithm is an improvement in the runtime of the Iterative scan algorithm. 
Implementation is quite similar to an Iterative scan except that the nodes that don't contribute to cluster density are ignored.

@author -  Vamshi Chidara (schidar), Akhil kumar Mengani (amengan), Nivedita lodha (nnlodha)
'''

import networkx as nx

# Calculate density of the community as metric
def community_weight(community):
	return float(2 * nx.number_of_edges(community) / nx.number_of_nodes(community))

#Improve communities detected by Link Aggregate Algorithm
def improved_iterative_scan_algo(community,graph):
	# Construct the subgraph corresponding to the input community
	community_graph = graph.subgraph(community)
	# Calculate the density of the community (metric)
	W = community_weight(community_graph)
	metric_increase = True

	while metric_increase:
		N = list(community_graph.nodes)

		for vertex in community_graph.nodes:
			N = list(set(N).union(set(graph.neighbors(vertex))))

		# check if the iterated vertex can increase the community density
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
				
			if W_prime > W:
				community_graph = community_graph_prime.copy()

		new_weight = community_weight(community_graph)

		if new_weight == W:
			metric_increase = False
		else:
			W = new_weight

	return list(community_graph.nodes)