class Node:
    def __init__(self,data):
        self.data=data
        self.nextadd=None

class Linkedlist:
    def __init__(self):
        self._head=None

    def insert(self,data):
        newnode = Node(data)

        if (self._head==None):
            self._head=newnode
        else:
             lastnode=self._head
             while(lastnode.next !=null):
                    lastnode=lastnode.nextadd

             lastnode.nextadd=newnode

    def display(self):
        # to display the nodes in ascending order
        currentnode=self._head
        while True:
            if(currentnode!=None):
                print(currentnode.data)
                currentnode=currentnode.nextadd
            else:
                break


 #Creating nodes below thats it
ll=Linkedlist()
ll.insert('Smit')
# s1=Node('Smit')
# s2=Node('Linkedlist')
# s3=Node('Being healthy is wealthy')

ll.display()






