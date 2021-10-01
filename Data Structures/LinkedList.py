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

    def insert_at_position(self,data,pos):
        temp = Node(data)
        p=self.head
        i=0
        while i < pos-1 and p.link:
            p = p.link
            i += 1
        if p is None:
            pass