class Node:
    def __init__(self,data,):
        self.data=data
        self.add=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def insert(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            lastnode=self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode=lastnode.add
                lastnode.add=newNode



