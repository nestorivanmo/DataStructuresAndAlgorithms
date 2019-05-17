from Graph import *;
import numpy as np
import random

# global variables
# totalGraph = [1,2,10,1,4,1,2,5,8,5,4,3,4,2,2,3,5,4,3,6,10,6,6,1]
totalGraph = [1,2,0,1,4,0,4,2,0,2,5,0,5,4,0,3,5,0,3,6,0,6,6,0]
g = Graph()
MAXV = 0
times = 0

colors = []
predecessors = []
distances = []
finishes = []
# Depth First Search algorithm
def depthFirstSearch(g):
    global times

    for u in range(g.numNodes+1):

            colors.append("White")
            predecessors.append(None)
            distances.append(0)
            finishes.append(0)
    times = 0
    for u in range(g.numNodes):

        if u > 0:
            if colors[u] == "White":
                print("Visiting u : " + str(u))
                visit(u)
    while colors !=[]:
        colors.pop(0)
    while predecessors !=[]:
        predecessors.pop(0)
    while distances !=[]:
        distances.pop(0)
    while finishes != []:
        finishes.pop(0)

# Function that visits all adjacent nodes to a node U
def visit(u):
    global times
    global colors
    global distances
    global finishes
    global predecessors


    colors[u] = "Gray"
    times += 1
    distances[u] = times
    # print("U " + str(u))
    # print(colors[u])
    v = g.edges[u]
    while v != None:
        
        V = v.to
        # print(str(u) + ":" + colors[u] + " -> " + str(V) + ":" + colors[V])
        if colors[V] == "White":
            predecessors[V] = u
            visit(V)
        v = v.previous

    colors[u] = "Black"
    times = times + 1
    finishes[u] = times

# Function
def printUpdatedGraph(g):
    print(" ")
    for u in range(1,len(g.edges)):
        print(str(u) + " " + colors[u]+" ( "+str(distances[u])+"/"+str(finishes[u]) + " )")

# Basic set up functions to start and create the graph
def setDirectedCostGraph():
    g.isDirected = True if int(input("Directed (1) ? Not Directed (2)? : ")) == 1 else False
    g.hasCost = True if int(input("Cost (1) ? No Cost (2)? : ")) == 1 else False

def setNumNodesNumEdgesAndCreateGraph():
    MAXV = int(input("Number of nodes: "))
    s=(MAXV,MAXV)
    matrix = np.zeros(s)
    startGraph(g, MAXV)
    g.numNodes = MAXV
    g.numEdges = int(input("Number of edges: "))
    createGraph(g, matrix, totalGraph)
    printGraph(g)


def createNewGraph(graph, max):
    graph.isDirected = True
    graph.hasCost = False
    max = len(r)
    startGraph(G, max)
    g.numNodes = max
    g.numEdges = int(input("Number of edges: "))
    createGraph(G, matrix, totalGraph)


# Main function
def main():
    setDirectedCostGraph()
    setNumNodesNumEdgesAndCreateGraph()
    depthFirstSearch(g)
    printUpdatedGraph(g)


main()
