'''
Implementation of Efficient Identification of Overlapping Communities
This file contains reading the input dataset file given as the command line argument
and running Link Aggregate Algorithm and Improved Iterative Scan Algorithm. 
Once the results are obtained, it writes the output to the results folder. 

@author -  Vamshi Chidara (schidar), Akhil kumar Mengani (amengan), Nivedita lodha (nnlodha)
'''

import sys
import networkx as nx
from link_aggregrate_algo import *
from improved_iterative_scan_algo import *

def get_file_name_from_file_path(file_path):
    output_file = file_path.split("/")
    return output_file[len(output_file)-1]

def main():
    graph = nx.Graph()
    data_file = sys.argv[1]
    with open(data_file) as file_ptr:
        next(file_ptr)
        for line in file_ptr:
            line = line.split()
            vertex1 = int(line[0])
            vertex2 = int(line[1])
            graph.add_edge(vertex1,vertex2)
    
    initial_communities = link_aggregrate_algorithm(graph)
    final_communities = []
    for community in initial_communities:
        final_communities.append(improved_iterative_scan_algo(community, graph))
    
    unique_final_communities = []
    for community in final_communities:
        community = sorted (community)
        if community not in unique_final_communities:
            unique_final_communities.append(community)
    
    output_file_name = get_file_name_from_file_path(data_file)
    output_path = "./results/"+output_file_name+".txt"

    with open(output_path, 'w') as file_ptr:
        for community in unique_final_communities:
            community_data = " ".join(map(str, community))
            file_ptr.write(community_data + '\n')


if __name__ == "__main__":
    main()