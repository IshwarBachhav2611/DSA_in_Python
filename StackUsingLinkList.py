class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

class Stack:
    def __init__(self):
        self.top = None

    # push operation
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(self.top.data," Added")


    #pop operation 
    def pop(self):
        if self.top == None:
            print("Stack is Empty...!")
            return
        
        print(self.top.data," Removed")
        self.top = self.top.next

    #Peek Operation 
    def peek(self):
        if self.top == None:
            print("Stack Underflow")
            return
        print("Top Element",self.top.data)

    # Display Operation 
    def display(self):
        if self.top == None:
            print("Stack Underflow...!")
            return
        temp = self.top
        print("Stack Elements:")
        while temp:
            print(temp.data,end="\n")
            temp = temp.next       
    


#----------Main----------
st = Stack()
st.push(10)
st.push(20)
st.push(30)
st.push(40)
st.push(50)
st.display()
st.pop()
st.peek()

        
