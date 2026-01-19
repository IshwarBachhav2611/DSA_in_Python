class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head == None:
            print("Linked List is Empty...!")
            return
        temp = self.head
        while temp:
            print(temp.data,end="<->")
            temp = temp.next 
        print("NULL")

    def insert_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        
    # Delete First Element
    def delete_begin(self):
        if self.head == None:
            print("Linked List is Empty...!")
            return
        
        if self.head :
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    # Delete Last Element
    def delete_end(self):
        if self.head == None:
            print("Liked List is Empty...!")
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    # Delete at Position 
    def delete_position(self,pos):
        if self.head == None:
            print("List is Empty...!")
            return
        
        if pos == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

        temp = self.head
        count = 0

        while temp and count<pos:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid Position...!")
            return
        
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next

    # Delete by Value 
    def delete_value(self, key):
        if self.head == None:
            print("List is Empty...!")
            return 
        
        temp = self.head
        while temp:
            if temp.data == key:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                return
            temp = temp.next
        
 
#----------Main----------
dll = DoublyLinkedList()
dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_end(40)
dll.insert_end(50)
dll.display()
dll.delete_begin()
dll.display()
dll.delete_end()
dll.display()
dll.delete_position(1)
dll.display()
dll.delete_value(20)
dll.display()

