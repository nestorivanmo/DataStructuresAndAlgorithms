from collections import Counter
from blocks.bookdetail import *
from sortManager.sortManager import *
class Node(object):
    def __init__(self, parent, k):
        self.key = k
        self.parent = parent
        self.left = None
        self.right = None
    def _str(self):
        label = str(self.key)
        if self.left is None:
            left_lines, left_pos, left_width = [], 0, 0
        else:
            left_lines, left_pos, left_width = self.left._str()
        if self.right is None:
            right_lines, right_pos, right_width = [], 0, 0
        else:
            right_lines, right_pos, right_width = self.right._str()
        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)
        if (middle - len(label)) % 2 == 1 and self.parent is not None and \
           self is self.parent.left and len(label) < middle:
            label += '.'
        label = label.center(middle, '.')
        if label[0] == '.': label = ' ' + label[1:]
        if label[-1] == '.': label = label[:-1] + ' '
        lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                 ' ' * left_pos + '/' + ' ' * (middle-2) +
                 '\\' + ' ' * (right_width - right_pos)] + \
          [left_line + ' ' * (width - left_width - right_width) + right_line
           for left_line, right_line in zip(left_lines, right_lines)]
        return lines, pos, width
    def __str__(self):
        return '\n'.join(self._str()[0])
    def find(self, k):
        if k == self.key:
            return self
        elif k < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(k)
        else:
            if self.right is None:  
                return None
            else:
                return self.right.find(k)
    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current
    def next_larger(self):
        if self.right is not None:
            return self.right.find_min()
        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current.parent
    def insert(self, node):
        if node is None:
            return
        if node.key < self.key:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node    
            else:
                self.right.insert(node)
    def delete(self):
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self
        else:
            s = self.next_larger()
            self.key, s.key = s.key, self.key
            return s.delete()
class Book(Node):
    def __init__(self, title, author, country, isbn, genre, details=None):
        super(Book, self).__init__(None, (title+"_"+author+"_"+isbn))
        self.title = title
        self.author = author
        self.country = country
        self.isbn = isbn 
        self.genre = genre 
        self.details = details
    def getBook(self):
        return (self.title+"|"+self.author+"|"+self.country+"|"+self.isbn+"|"+self.genre+"|"+str(self.details))
    def updateDetails(self,content):
        if self.details is None:
            self.details = [content]
        else:
            self.details.append(content)
class User(Node):
    sortManager = SortManager()
    personalLibrary = []
    def __init__(self, name, lastname, email, password, city, country,rentingBooks=None):
        super(User, self).__init__(None, email)
        self.name = name 
        self.lastname = lastname
        self.email = email 
        self.password = password
        self.city = city
        self.country = country
        self.rentingBooks = rentingBooks
    def getUser(self):
        return (self.name+"|"+self.lastname+"|"+self.email+"|"+self.password+"|"+self.city+"|"+self.country+"|"+str(self.rentingBooks))
    def getPersonalLibrary(self):
        return self.personalLibrary
    def updateRentingBooks(self, content):        
        booksToSort = self.rentingBooks
        if booksToSort is None:
            booksToSort = [content]
        else:
            booksToSort.append(content)
        booksToSort = self.sortManager.dataToSort(booksToSort)
        self.rentingBooks = booksToSort
