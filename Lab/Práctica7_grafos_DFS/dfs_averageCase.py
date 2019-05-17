import random
import matplotlib.pyplot as plt
class Node:
    to = 0
    previous = None
    cost = 0
    color = "White"
    distance = 0
    finish = 0
    predecessor = None

class Graph:
    edges = []
    grades = []
    numNodes = 0
    numEdges = 0
    isDirected = False
    hasCost = False


def startGraph(g, MAXV):
    i = 0
    while i <= MAXV:
        g.grades.append(0)
        i += 1
    i = 0
    while i <= MAXV:
        g.edges.append(None)
        i += 1

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


colors = []
predecessors = []
distances = []
finishes = []

# Depth First Search algorithm
def depthFirstSearch(g,d):
    global yiteraciones
    global times
    for u in range(d):
            yiteraciones=yiteraciones+1
            colors.append("White")
            predecessors.append(None)
            distances.append(0)
            finishes.append(0)
    times = 0
    for u in range(g.numNodes):
        yiteraciones=yiteraciones+1
        if u > 0:
            if colors[u] == "White":
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
    global yiteraciones

    colors[u] = "Gray"
    times += 1
    distances[u] = times
    v = g.edges[u]
    while v != None:
        yiteraciones += 1
        V = v.to
        if colors[V] == "White":
            predecessors[V] = u
            visit(V)
        v = v.previous

    colors[u] = "Black"
    times = times + 1
    finishes[u] = times


listaU=[]
listaV=[]
def averageCase(g):
    n=g.numNodes
    g.numEdges=(n/2)
    listaU =[0]  * (n-1)
    listaV =[0]  * (n-1)
    listaC =[0]  * (n-1)

    for i in range(n-1):
        listaU[i] = random.randint(1,500)
    for i in range(n-1):
        listaV[i] = random.randint(1,500)
    for i in range(n-1):
        listaC[i] = random.randint(1,500)
    b=max(listaU)
    c=max(listaV)
    d=max(c,b)
    startGraph(g,d)
    t=cost=0

    while t <( n-1):
        u = listaU[t]
        v = listaV[t]
        if g.hasCost==True:
            cost = listaC[t]
        else:
            cost=1

        insertEdge(g,u,v,cost,g.isDirected)
        t=t+1
    depthFirstSearch(g,d)





def main(n,g):
    g.isDirected = True
    g.hasCost =False
    g.numNodes = n
    g.numEdges=0

    averageCase(g)





n=100
elementosx=[]
tiempoy=[]

g=Graph()
for l in range(2,n+1,2):
    times=0
    yiteraciones=0
    main(l,g)

    g.edges = []
    g.grades = []
    g.numNodes = 0
    g.numEdges = 0
    g.isDirected = False


    elementosx.append(l)

    tiempoy.append(yiteraciones)
    plt.plot(elementosx,tiempoy,color="b")
