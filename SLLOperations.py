# Singly Linked List - Search, Count, Reverse

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert End 
    def insert_end(self,data):
        new_node = Node(data)
        if self.head == None:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next 
        temp.next = new_node

    # Display List 
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")

    # Search
    def search(self,key):
        temp = self.head
        
        if temp and temp.data == key:
            print(f"{key} found at location Node-1")
            count += 1
            return
        count = 1
        while temp.next:
            if temp.next.data == key:
                print(f"{key} found at Node-{count}")
                return
            count += 1 
            temp = temp.next 
        print(f"{key} is Not present in Nodes...!")

    # Count Nodes
    def count_node(self):
        if self.head == None:
            print("List is Empty...!")
            return
        
        temp = self.head
        count = 0
        while temp:
            count +=1
            temp = temp.next
        print("No. of Nodes :",count)


    # Reverse List
    def reverse_list(self):
        current = self.head
        prev = 0
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# -------- MAIN --------
sll = SinglyLinkedList()
sll.insert_end(10)
sll.insert_end(20)
sll.insert_end(30)
sll.insert_end(40)
sll.insert_end(50)
sll.reverse_list()
sll.display()
sll.search(10)
sll.count_node()




