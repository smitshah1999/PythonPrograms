class node:         #Creating a class to design linked list structure
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:  #Creating a Linked List class
    def __init__(self):
        self.head=None
        self.tail=None

    def addNode(self,data): # Creating addnode to create nodes
        newnode=node(data)
        if(self.head ==None):
            self.head=newnode #Here both head and tail will point  to new node since no nodes are available
            self.tail=newnode
        else:
            self.tail.next=newnode  #Here Tail will point to the new node
            self.tail=newnode #Here tail will move to the new node

    def deleteatstart(self):
        if(self.head==None): #Here we are checking if the linked list is empty or not.
            print("linkedlist is emty")
        else:
            if(self.head !=self.tail):
                self.head=self.head.next
            else:
                self.head=self.tail=None

    def display(self):
        current=self.head
        if(self.head==None):
            print("List is empty")
        while(current!=None):
            print(current.data,end="")
            current=current.next
            print()

sList=Linkedlist()
 # Adds data to the list
sList.addNode(1)
sList.addNode(2)
sList.addNode(3)
sList.addNode(4)
    # Printing original list
print("Original List: ")
sList.display()

while (sList.head != None):
        sList.deleteatstart()
        # Printing updated list
        print("Updated List: ")
        sList.display();














