class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def addnode(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
          #  self.tail=newnode
        else:
            # //without tail
            temp=self.head
            while(temp.next !=None):
              temp=temp.next

            temp.next = newnode

            # // with tail
            #    tail.next = newnode
            #     tail = tail.next
            #

        def findSize(self):
            count=1
            while(temp.next!=null):
                count=count+1
                return count()






ab   |3|bc|
bc   |4|ef|
ef   |5|none|
hj   |6|none|


HEAD
temp

   3-->4-->5-->6-->7-->

addnode(3)
addnode(4)
addnode(5)
addnode(6)







