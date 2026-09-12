class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert1st(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def display(self):
        temp=self.head
        while temp:
            print(f'{temp.data} -> ',end='')
            temp=temp.next


Linked=LinkedList()
Linked.insert1st(1)
Linked.insert1st(2)
Linked.insert1st(3)
Linked.insert1st(4)
Linked.display()