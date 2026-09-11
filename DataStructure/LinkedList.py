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

    def displayList(self):
        temp=self.head
        while temp:
            print(f'{temp.data} ->',end='')
            temp=temp.next 

myLinkedList=LinkedList()
myLinkedList.insert1st(1)
myLinkedList.insert1st(2)
myLinkedList.insert1st(3)
myLinkedList.insert1st(4)
myLinkedList.displayList()

