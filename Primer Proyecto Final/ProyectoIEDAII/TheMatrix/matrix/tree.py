import random, sys
from blocks.node import Node
def height(node):
    if node is None:
        return -1
    else:
        return node.height
def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1
class AVL(object):
    treeAsList = []
    def __init__(self):
        self.root = None
    def __str__(self):
        if self.root is None: 
            return
        return str(self.root)
    def find(self, k):
        return self.root and self.root.find(k)
    def find_min(self):
        return self.root and self.root.find_min()
    def next_larger(self, k):
        node = self.find(k)
        return node and node.next_larger()   
    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        update_height(x)
        update_height(y)
    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        update_height(x)
        update_height(y)
    def rebalance(self, node):
        while node is not None:
            update_height(node)
            if height(node.left) >= 2 + height(node.right):
                if height(node.left.left) >= height(node.left.right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif height(node.right) >= 2 + height(node.left):
                if height(node.right.right) >= height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.parent
    def insert(self, node):
        node = node
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)
        self.rebalance(node)
    def delete(self, k):
        node = self.find(k)
        if node is None:
            return None
        if node is self.root:
            pseudoroot = Node(None, ' ') 
            pseudoroot.left = self.root
            self.root.parent = pseudoroot
            deleted = self.root.delete()
            self.root = pseudoroot.left
            if self.root is not None:
                self.root.parent = None
        else:
            deleted = node.delete()  
        self.rebalance(deleted.parent)
        return deleted

    def orderedTreeWalk(self,node):
        if node is not None:
            self.orderedTreeWalk(node.left)
            self.treeAsList.append(node.key)
            self.orderedTreeWalk(node.right)
        return self.treeAsList