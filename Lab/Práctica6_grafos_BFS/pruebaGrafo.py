import numpy as np

# totalGraph = [1,5,1,1,2,1,1,7,1,1,6,2,1,11,1,1,9,1,1,12,1,2,7,1,2,6,1,2,5,1,2,19,1,2,3,1,2,9,1,2,12,1,3,4,2,5,18,1,5,6,1,5,8,1,5,7,1,5,20,1,6,13,1,6,9,1,6,12,1,7,8,2,7,10,1,8,10,2,8,13,2,8,18,1,9,11,1,9,12,1,10,13,1,10,12,1,11,12,1,11,17,2,11,15,1,12,17,2,12,15,1,13,14,1,13,16,1,13,18,2,14,16,1,14,18,1,15,17,2,16,18,2]
# totalGraph = [1,2,10,2,3,10,3,4,10,4,5,10,4,6,10,5,6,10,6,8,10,5,8,10,5,7,10,7,8,10]
# totalGraph = [2,1,10,3,2,10,3,4,10]

class Node:
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
        insertEdge(g,u,v,cost,g.isDirected)
        matrix[u-1][v-1] = cost
        if g.isDirected == False:
            matrix[v-1][u-1] = cost
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

def insertEdge(g,u,v,cost,isDirected):
    item = Node()
    item.to = v
    item.previous = g.edges[u] #None para el primer elemento
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


cola = []
contador = 0
def BFS(G, intS):

    global contador
    G.edges[intS].color = "Gray"
    G.edges[intS].distance = 0

    cola.append(G.edges[intS])

    while len(cola) != 0:
        U = cola.pop(0)
        V = U
        while U != None:
            contador += 1
            if G.edges[U.to] != None:
                if G.edges[U.to].color == "White":
                    G.edges[U.to].color = "Gray"
                    G.edges[U.to].distance = V.distance + 1
                    cola.append(G.edges[U.to])
            U = U.previous
        V.color = "Black"

    for i in range(G.numNodes + 1):
        if G.edges[i] != None:
            print(str(i) + " - " + G.edges[i].color + ":"+ str(G.edges[i].distance))


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
    print("Graph length: " + str(len(g.edges)))
    printGraph(g)
    BFS(g,3)



    # print(contador)
    # for x in range(g.numNodes-1):
    #     BFS(g,x)
    #     print("---------------------")

mainAdyacentList()
