# Singly Linked List - Insert Operations

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")

    # Insert at Beginning
    def insert_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at End
    def insert_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node   

    # Insert at Position
    def insert_position(self,pos,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        count = 0
        for _ in range(pos-1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        
# -------- MAIN --------
sll = SinglyLinkedList()
sll.insert_begin(20)
sll.insert_begin(10)
sll.insert_end(30)
sll.insert_end(40)
sll.insert_position(2,25)
sll.display()
