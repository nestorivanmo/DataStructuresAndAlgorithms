class Node:
	to = 0
	cost = 0
	nxt = None 

class Graph: 
	edges = []
	grades = []
	numNodes = 0
	numEdges = 0
	isDirected = False 	

startGraph(graph)


def main():
	graph = Graph()
	graph.isDirected = True if int(input("Directed Graph (1) ? Not Directed(2)")) == 1 else False
	graph.numNodes = int(input("Number of nodes"))
	graph.numEdges = int(input("Number of edges"))
	

main()
		
