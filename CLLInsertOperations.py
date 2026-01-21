class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Display
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(HEAD)")

    # Insert at Beginning
    def insert_begin(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            new.next = new
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        new.next = self.head
        temp.next = new
        self.head = new

    # Insert at End
    def insert_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            new.next = new
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new
        new.next = self.head
        
#----------Main----------
cll = CircularLinkedList()
cll.insert_begin(10)
cll.insert_begin(20)
cll.insert_begin(30)
cll.insert_begin(40)
cll.display()

