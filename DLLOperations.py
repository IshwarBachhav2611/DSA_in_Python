class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Display List Forword
    def display_front(self):
        if self.head == None:
            print("List is Empty...!")
            return
        
        temp = self.head
        print("Display Forword...")
        print("NULL",end="<->")
        while temp:
            print(temp.data,end="<->")
            temp = temp.next
        print("NULL")

    # Display list Backword
    def display_back(self):
        if self.head == None:
            print("List is Empty...!")
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        print("Display Reverse...!")
        print("NULL",end="<->")
        while temp:
            print(temp.data,end="<->")
            temp = temp.prev
        print("NULL",end="<->")

    # Count_Nodes
    def count(self):
        count = 1
        temp = self.head
        while temp.next:
            count += 1
            temp = temp.next
        print("Total Nodes :",count)

    # Search Element
    def search(self,key):
        temp = self.head
        count = 1
        if temp.data == key:
            print(temp.data,"is at location",count)

        while temp:
            if temp.data == key:
                print(temp.data,"is at location:",count)
                return
            count += 1
            temp = temp.next
        print(f"{key} is Not present in List...!")


    # Insert Element at End
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



#----------Main----------
dll = DoublyLinkedList()
dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_end(40)
dll.insert_end(50)
dll.insert_end(60)
dll.count()
dll.search(30)
dll.display_front()
dll.display_back()

            