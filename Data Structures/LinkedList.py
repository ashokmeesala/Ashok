class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head=None

    def display_list(self):
        if self.head is None:
            print('Empty list')
        else:
            print('List is')
            p = self.head
            while p:
                print(p.data,end=' ')
                p = p.link
            print()

    def count_nodes(self):
        count = 0
        p = self.head
        while p:
            p = p.link
            count +=1
        print('Number node are ',count)

    def search(self, data):
        p = self.head
        pos = 0
        while p:
            pos += 1
            if p.data == data:
                print(data,'is found at ',pos)
                break
            p = p.link     
        else:
            print(data,'is not found')


    def insert_in_begning(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
        else:
            temp.link = self.head
            self.head = temp

    def insert_at_end(self, data):
        temp = Node(data)
        if self.head is None:
            self.insert_in_begning(data)
            return
        p = self.head
        while p.link:
            p = p.link
        p.link = temp

    def create_list(self):
        non = int(input('Enter no of nodes '))
        for i in range(non):
            data = eval(input('enter data to be inserted '))
            self.insert_at_end(data)

    def insert_at_position(self,pos,data):
        temp = Node(data)
        if pos == 0:
            self.insert_in_begning(data)
            return
        if self.head is None:
            print("Empty List")
            return
        p = self.head
        i = 0
        while i < pos and p:
            if i == pos-1:
                temp.link = p.link
                p.link = temp
                break
            p = p.link
            i += 1
        if p is None:
            print(pos,'longer than list length')

    def insert_before_node(self,data,x):
        temp = Node(data)
        if self.head.data == x:
            self.insert_in_begning(data)
            return
        p = self.head
        while p.link:
            if p.link.data == x:
                temp.link = p.link
                p.link = temp
                break
            p = p.link
        else:
            print(x,'Not found')

    def insert_after_node(self,data,x):
        temp = Node(data)
        p = self.head
        while p:
            if p.data == x:
                temp.link = p.link
                p.link =temp
                break
            p = p.link
        else:
            print(x,"Not found")

    def reverse_list(self):
        p = self.head
        prev = None
        while p:
            next = p.link
            p.link = prev
            prev = p
            p = next
        self.head = prev
