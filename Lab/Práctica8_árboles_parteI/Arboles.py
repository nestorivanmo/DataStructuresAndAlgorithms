# class Node:
#     def __init__(self, value):
#         self.leftSon = None
#         self.rightSon = None
#         self.val = value
#
# class Tree:
#     def __init__(self):
#         self.root = None
#
#     def getRoot(self):
#         return self.root
#
#     def addNode(self, val):
#         if self.root == None:
#             self.root = Node(val)
#         else:
#
import random
key = ['','+','*','^', 'A', 'B','/', '3', '','','','', 'C', 'D']

orderCounter = 0
preOrderCounter = 0
posOrderCounter = 0

def left(x):
    return 2*x

def right(x):
    return (2*x) + 1

def orderedTreeWalk(x, tree):
    global orderCounter
    if x < len(tree):
        orderCounter += 1
        orderedTreeWalk(left(x), tree)
        print(tree[x])
        orderedTreeWalk(right(x),tree)

def preOrderedTreeWalk(x, tree):
    if x < len(tree):
        print(tree[x])
        preOrderedTreeWalk(left(x),tree)
        preOrderedTreeWalk(right(x),tree)

def postOrderedTreeWalk(x, tree):
    if x < len(tree):
        postOrderedTreeWalk(left(x),tree)
        postOrderedTreeWalk(right(x),tree)
        print(tree[x])


def generateTree():
    tree = ['']
    for x in range(1,10):
        tree.append(x)

    print("Inorder Tree Walk")
    orderedTreeWalk(1, tree)
    print("Preorder Tree Walk")
    preOrderedTreeWalk(1, tree)
    print("Postorder Tree Walk")
    postOrderedTreeWalk(1, tree)

def main():
    generateTree()

main()
