import numpy as np

totalGraph = [0,4,1,0,1,1,0,6,1,0,5,2,0,10,1,0,8,1,0,11,1,1,6,1,1,5,1,1,4,1,1,18,1,1,2,1,1,8,1,1,11,1,2,3,2,4,17,1,4,5,1,4,7,1,4,6,1,4,19,1,5,12,1,5,8,1,5,11,1,6,7,2,6,9,1,7,9,2,7,12,2,7,17,1,8,10,1,8,11,1,9,12,1,9,11,1,10,11,1,10,16,2,10,14,1,11,16,2,11,14,1,12,13,1,12,15,1,12,17,2,13,15,1,13,17,1,14,16,2,15,17,2]

class Node:
    id = 0
    to = 0
    previous = None
    cost = 0
    distance = -1
    color = "White"

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


def createGraph(g, matrix):
    k = 0
    u = 0
    v = 0
    cost = 0
    i = 0
    while k < len(totalGraph):
        u = totalGraph[k]
        v = totalGraph[k+1]
        cost = totalGraph[k+2]
        insertEdge(g,u,v,cost,g.isDirected, i)
        matrix[u-1][v-1] = cost
        if g.isDirected == False:
            matrix[v-1][u-1] = cost
        i += 1
        k += 3
    # i = 0
    # num = g.numEdges
    # while i < num:
    #   u = int(input("u : "))
    #   v = int(input("v : "))
    #   if g.hasCost == True:
    #     cost = int(input("Cost: "))#cost2
    #   else:
    #     cost = 1
    #   insertEdge(g,u,v,cost,g.isDirected)
    #   matrix[u-1][v-1] = cost
    #   if g.isDirected == False:
    #       matrix[v-1][u-1] = cost
    #       i += 1




def insertEdge(g,u,v,cost, isDirected, id):
    item = Node()
    item.id = id
    item.to = v
    item.previous = g.edges[u] #None para el primer elemento
    item.cost = cost
    g.edges[u] = item
    g.grades [u] += 1
    if isDirected == False and v != u:
        insertEdge(g,v,u,cost, True, id)
    else:
        g.numEdges += 1

def printGraph(g):
    i=0
    item =  None
    string = ""
    while i<g.numNodes:
        string += str(i) + "\t"
        item = g.edges[i]
        while item != None:
            string += str(item.to) + " : " + str(item.cost) + "\t"
            item = item.previous
        string += "\n"
        i += 1
    print(string)


cola = []
def BFS(G, intS):
    G.edges[intS].color = "Gray"
    G.edges[intS].distance = 0

    cola.append(G.edges[intS])

    while len(cola) != 0:
        U = cola.pop(0)
        U.color = "Black"
        while U != None:
            V = G.edges[U.to]
            if V.color == "White":
                V.color = "Gray"
                V.distance = U.distance + 1
                V.previous = U
                cola.append(V)
            U = U.previous
    


def mainAdyacentList():
    g = Graph()
    g.isDirected = True if int(input("Directed (1) ? Not Directed (2)? : ")) == 1 else False
    g.hasCost = True if int(input("Cost (1) ? No Cost (2)? : ")) == 1 else False
    MAXV = int(input("Number of nodes: "))
    s=(MAXV,MAXV)
    matrix = np.zeros(s)
    startGraph(g, MAXV)
    g.numNodes = MAXV
    g.numEdges = int(input("Number of edges: "))
    createGraph(g, matrix)
    printGraph(g)
    BFS(g,5)

mainAdyacentList()
