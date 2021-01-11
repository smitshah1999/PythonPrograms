class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;


class SinglyLinkedList:
    # Represent the head and tail of the singly linked list
    def __init__(self):
        self.head = None;
        self.tail = None;

        # addNode() will add a new node to the list

    def addNode(self, data):
        # Create a new node
        newNode = Node(data);

        # Checks if the list is empty
        if (self.head == None):
            # If list is empty, both head and tail will point to new node
            self.head = newNode;
            self.tail = newNode;
        else:
            # newNode will be added after tail such that tail's next will point to newNode
            self.tail.next = newNode;
            # newNode will become new tail of the list
            self.tail = newNode;

    def Removeduplicates(self):
        current=self.head

        while current is not None:
            temp = current
            while temp.next is not None:
              #  print(temp.data)
                if (current.data == temp.next.data):
                    temp.next = temp.next.next
                temp=temp.next
            current=current.next

            # else:
            #     temp = temp.next
            # # if(temp.data==current.data):
            # #     temp=temp.next.next
            # # temp=temp.next
            # current=current.next


    def display(self):
        # to display the nodes in ascending order
        currentnode = self.head
        while True:
            if (currentnode != None):
                print(currentnode.data)
                currentnode = currentnode.next
            else:
                break

#Broke the class and main program begins
nList=SinglyLinkedList()
nList.addNode(1)
nList.addNode(1)
nList.addNode(2)
nList.addNode(3)
nList.addNode(41)
nList.addNode(2)
nList.addNode(3)
nList.addNode(5)
nList.addNode(6)
nList.Removeduplicates()
nList.display()



