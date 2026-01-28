class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # EnQueue Element
    def enqueue(self,data):
        new_node = Node(data)
        if self.rear == None:
            self.front = self.rear = new_node
            print(f"{data} inserted")
            return
        
        self.rear.next = new_node
        self.rear = new_node
        print(f"{data} inserted")

    #Dequeue Operation
    def dequeue(self):
        if self.front == None:
            print("Queue is Empty...!")
            return
        
        removed = self.front.data
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        print(f"{removed} Removed")
        

    # peek operation
    def peek(self):
        if self.rear == None:
            print("Queue is Empty")
            return
        print(f"Front Element: {self.front.data}")

    # display Queue
    def display(self):
        if self.rear == None:
            print("Queue is Empty...!")
            return
        
        temp = self.front
        print("Queue Elements :")
        while temp:
            print(f"{temp.data}",end=" ")
            temp = temp.next
        print("")

        
#----------Main----------
que = Queue()
que.enqueue(10)
que.enqueue(20)
que.enqueue(30)
que.enqueue(40)
que.enqueue(50)
que.display()
que.peek()
que.dequeue()
que.display()
que.peek()


