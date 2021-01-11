# Represent a node of the singly linked list
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

            # display() will display all the nodes present in the list

    def minNode(self):
        current = self.head

        if (current == None):
            print('List is empty')
            return
        else:
            print('else is printed')
            while (current.next != None):
                print(current.data)
                if (current.data < current.next.data):
                    min = current.data
                current = current.next


        print("Minimum Node=" + str(min))

    def MaxNode(self):
        current=self.head
        if(current==None):
            print('List is empty')
            return
        else:
            while(current.next!=None):
                print(current.data)
                if(current.data>current.next.data):
                    max=current.data
                    current=current.next
                print("Maximum node="+str(max))


# Code execution starts here
sList = SinglyLinkedList();

# Add nodes to the list
sList.addNode(1);
sList.addNode(2);
sList.addNode(3);
sList.addNode(4);
sList.minNode();
sList.MaxNode();
# Displays the nodes present in the list
