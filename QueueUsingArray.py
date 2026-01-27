class Queue:
    def __init__(self,size):
        self.queue = []
        self.size = size
        self.front = -1
        self.rear = -1

    # Insert Element
    def enqueue(self,data):
        if self.rear == self.size - 1:
            print("Queue is Full...!")
            return
        if self.front == -1:
            self.front = 0

        self.queue.append(data)
        self.rear += 1
        print(f"{self.queue[self.rear]} Added")
 
    # Remove Element 
    def dequeue(self):
        if self.rear == -1:
            print("Queue is Empty...!")
            return
        
        print(self.queue.pop(self.front)," Removed")
        self.rear -= 1

    # PEEK Operation 
    def peek(self):
        if self.rear == -1:
            print("Queue is Empty...!")
            return 
        element = self.front
        print(f"Front Element :{self.queue[element]}")


    # Display operation
    def display(self):
        if self.rear == -1:
            print("Queue is Empty..!")
            return
        
        for i in range(self.front,self.rear +1):
            print(self.queue[i],end=" ")
        print("")


             
#----------Main----------
que = Queue(5)
que.enqueue(10)
que.enqueue(20)
que.enqueue(30)
que.enqueue(40)
que.enqueue(50)
que.display()
que.peek()
que.dequeue()
que.peek()
que.display()

