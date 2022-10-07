# Efficient Identification of Overlapping Communities

Team:
Vamshi Chidara (schidara), Akhil Kumar Mengani (amengan), Nivedita Lodha(nnlodha)

Project Details:
This project is an efficient implementation of an algorithm for finding overlapping communities in social networks with better quality.
Paper Link

There are 3 python files mainly,
overlapping_communities.py
link_aggregrate_algo.py
improved_iterative_scan_algo.py

The purpose of each file is explained below.

This implementation consists of two algorithms,
Link Aggregate Algorithm: link_aggregrate_algo.py
This is a seed algorithm that captures good initial clusters.
Since IS performs well when the initial clusters are good, this algorithm needs to be efficient.
Improved Iterative Scan Algorithm: improved_iterative_scan_algo.py
Improved Iterative Scan Algorithm is an improvement in the runtime of the Iterative scan algorithm. Implementation is quite similar to an Iterative scan except that the nodes that don't contribute to cluster density are ignored.

overlapping_communities.py : contains reading the input dataset file given as the command line argument and running Link Aggregate Algorithm and Improved Iterative Scan Algorithm. Once the results are obtained, it writes the output to the results folder. 

1. Software Requirements:
Python 3.8.8

Libraries:
sys : comes default with python
operator: comes default with python
networkx - 2.8.7 : to install networks, run  pip install networkx in the terminal.

2. Environment Variables: None

3. Instructions To Run:
Command: python <file.py> <dataset-file>

The Datasets folder contains different types of graphs (Amazon, DBLP, YouTube). Each type of graph will have different sizes like small, medium, large and original graphs. 

<file.py> : overlapping_communities.py 
<dataset-file>: command line argument should be substituted with the appropriate file name from the datasets folder before running the command.
 
Example to run Amazon small graph:
python overlapping_communities.py ./datasets/amazon/amazon.graph.small

Example to run DBLP small graph:
python overlapping_communities.py ./datasets/dblp/dblp.graph.small

Example to run YouTube small graph:
python overlapping_communities.py ./datasets/youtube/youtube.graph.small

4. Input and Output Files:
After running the command as given in 3. Instructions To Run , outputs are written to the result folder. An output file with the same name as the input dataset-file is created in the results folder.
Example:
When 
python overlapping_communities.py ./datasets/amazon/amazon.graph.small is run, output is written to /results/amazon.graph.small file.

The output file will look something as follows:
197 198 199 2860
997 998 999 1000 2645
56 57 59 61 1390 1426
1236 2264 2817 2823 2825
.
.

Each line consists of nodes (node identifiers) that belong to the same community. If we look at the above sample output, community 1 consists of 4 nodes, community 2 and 3 consists of 5 nodes where as community 4 consists of 5 nodes.

