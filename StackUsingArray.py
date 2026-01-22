class Stack:
    def __init__(self,size):
        self.stack = []
        self.size = size
        self.top = -1
    
    #Push operation 
    def push(self,data):
        if self.top == self.size-1:
            print("Stack Overflow...!")
            return
        
        self.stack.append(data)
        self.top += 1 
        print(f"{data} pushed")

    #Pop Operation
    def pop(self):
        if self.top == -1:
            print("Stack Underflow...!")
            return
        
        poped = self.stack.pop()
        self.top -= 1
        print(f"{poped} is Poped")

    #Peek Operation 
    def peek(self):
        if self.top == -1:
            print("Stack Underflow...!")
            return
        print("Top Element :",self.stack[self.top])

    #Display operation
    def display(self):
        if self.top == -1:
            print("Stack Underflow")
            return
        print("Stack Elements")
        for i in range(self.top,-1,-1):
            print(self.stack[i],end="\n")

    # check overflow
    def is_full(self):
        return self.top == self.size-1
    #check underflow
    def is_empty(self):
        return self.top == -1
    
#----------Main----------
st = Stack(5)
st.push(10)
st.push(20)
st.push(30)
st.push(40)
st.push(50)
st.peek()
st.display()
st.pop()
st.pop()
st.display()


