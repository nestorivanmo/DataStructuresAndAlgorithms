import random

class Node:
    def __init__(self, d):
        self.sons = list()
        self.keys = list()
        self.leaf = 1
        self.n = 0
        for k in range(2*d):
            self.keys.append(None)
        for k in range(2*d + 1):
            self.sons.append(None)

class BTree:
    def __init__(self,grade):
        self.d = grade
        self.root = None

    def createTree(self):
        if self.root == None:
            self.root = Node(self.d)
        return self.root

    def split_b_tree(self, x, i):
        z = Node(self.d)
        y = x.sons[i]
        z.leaf = y.leaf
        z.n = self.d-1
        for j in range(1, self.d):
            z.keys[j] = y.keys[j+self.d]
            y.keys[j+self.d] = None
        if y.leaf == 0:
            for j in range(1, self.d+1):
                z.sons[j] = y.sons[j + self.d]
                y.sons[j + self.d] = None

        y.n = self.d - 1
        for j in range(x.n + 1, i, -1):
            x.sons[j+1] = x.sons[j]
        x.sons[i+1] = z

        for j in range (x.n, i-1, -1):
            x.keys[j+1] = x.keys[j]

        x.keys[i] = y.keys[self.d]
        y.keys[self.d] = None
        x.n = x.n + 1

    def insert_non_full_b_tree(self, x, k):
        i = x.n
        if x.leaf == 1:
            # print("Llego -> " + str(x.keys))
            while i >= 1 and k < x.keys[i]:
                x.keys[i+1] = x.keys[i]
                i -= 1
            x.keys[i+1] = k
            x.n = x.n + 1
            # print("Sale -> " + str(x.keys))
        else:
            while i >= 1 and k < x.keys[i]:
                i -= 1
            i += 1
            if x.sons[i].n == 2*self.d - 1:
                self.split_b_tree(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full_b_tree(x.sons[i], k)

    def insert_b_tree(self, k):
        r = self.root
        # print("r.n " + str(r.n))
        if r.n == 2*self.d -1:
            s = Node(self.d)
            self.root = s
            s.leaf = 0
            s.n = 0
            s.sons[1] = r
            self.split_b_tree(s, 1)
            self.insert_non_full_b_tree(s, k)
        else:
            self.insert_non_full_b_tree(r, k)


def imprimir(act,tab):
    print(("   "*tab)+"")
    for i in range(1,len(act.keys)):
        if(act.keys[i]!=None):
            print(("   "*tab)+str(act.keys[i]))
    print(("   "*tab)+"")
    if(act.leaf != 1):
        for i in range(1,len(act.sons)):
            if(act.sons[i]!= None):
                imprimir(act.sons[i],tab+1)


def main():
    bt = BTree(2)
    bt.createTree()

    n = 10
    for x in range(10):
        r = random.randint(65,90)
        bt.insert_b_tree(r)

    

main()
