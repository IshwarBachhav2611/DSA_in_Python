# Singly Linked List - Delete Operations

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Display List 
    def display(self):
        if self.head == None:
            print("List is Empty...!")

        temp = self.head
        while temp:
            print(temp.data,end=" -> ")
            temp = temp.next 
        print("NULL")

    # Insert at end
    def insert_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node 

    # delete at begining 
    def delete_begin(self):
        if self.head == None:
            print("Linked list is Empty...!")
            return
        self.head = self.head.next 

    # Delete at end
    def delete_end(self):
        if self.head == None:
            print("Linked List is Empty")
            return
        
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    # Delete by Value 
    def delete_value(self,key):
        if self.head == None:
            print("Linked List is Empty :")

        temp = self.head
        if temp and temp.data == key:
            self.head = self.head.next
            return

        while temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
                return 
            temp = temp.next



# -------- MAIN --------
sll = SinglyLinkedList()
sll.insert_end(10)
sll.insert_end(20)
sll.insert_end(30)
sll.insert_end(40)

#sll.delete_begin()
sll.display()

#sll.delete_end()
sll.display()

sll.delete_value(30)
sll.display()