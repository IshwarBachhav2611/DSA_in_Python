# Doubly Linked List - Insert Operations + Display

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Display Forward
    def display(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("NULL")

    # Insert at Beginning
    def insert_begin(self, data):
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node  

    # Insert at End
    def  insert_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        new_node.prev = temp
        temp.next = new_node

    # Insert at Position
    def insert_position(self,key,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        for _ in range(key-1):
            temp = temp.next
        new_node.prev = temp
        new_node.next = temp.next
        temp.next = new_node


# -------- MAIN --------
dll = DoublyLinkedList()
dll.insert_begin(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_begin(6)
dll.insert_position(2,15)
dll.display()


