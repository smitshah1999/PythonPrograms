class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def addnode(self,data):
        newnode=node(data)
        if(self.head==None):
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode



'''
3-->4

'''
