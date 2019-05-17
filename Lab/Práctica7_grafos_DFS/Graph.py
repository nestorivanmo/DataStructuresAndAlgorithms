from Node import *;

class Graph:
    edges = []
    grades = []
    numNodes = 0
    numEdges = 0
    isDirected = False
    hasCost = False

def startGraph(g, MAXV):
    g.numNodes = 0
    g.numEdges = 0
    i = 0
    while i <= MAXV:
        g.grades.append(0)
        i += 1
    i = 0
    while i <= MAXV:
        g.edges.append(None)
        i += 1

def createGraph(g, matrix, totalGraph):
    k = 0
    u = 0
    v = 0
    cost = 0
    i = 0
    while k < len(totalGraph):
        u = totalGraph[k]
        v = totalGraph[k+1]
        if g.hasCost == True:
            cost = totalGraph[k+2]
        insertEdge(g,u,v,cost,g.isDirected)
        # matrix[u-1][v-1] = cost
        # if g.isDirected == False:
            # matrix[v-1][u-1] = cost
        k += 3

def insertEdge(g,u,v,cost,isDirected):
    item = Node()
    item.to = v
    item.previous = g.edges[u]
    item.cost = cost
    g.edges[u] = item
    g.grades [u] += 1
    if isDirected == False and v != u:
        insertEdge(g,v,u,cost, True)
    else:
        g.numEdges += 1

def printGraph(g):
    i=1
    item =  None
    string = ""
    while i<=g.numNodes:
        string += str(i) + "\t"
        item = g.edges[i]
        while item != None:
            string += str(item.to) + " : " + str(item.cost) + "\t"
            item = item.previous
        string += "\n"
        i += 1
    print(string)
