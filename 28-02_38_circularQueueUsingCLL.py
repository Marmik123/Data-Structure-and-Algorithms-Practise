#IMPLEMENTING CIRCULAR QUEUE USING CIRCULAR LINKED LIST.

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Queue:
    
    def __init__(self):
        self.front=None
        self.rear=None
    
    def enQueue(self,value):
        temp=Node(value)
        # temp.data=
        if self.front==None:
            self.front=temp
        else:
            self.rear.next=temp
        self.rear=temp
        self.rear.next=self.front
        
    def deQueue(self):
        value=None
        if self.front==None:
            print('QUEUE IS EMPTY')
            return -1
        if self.front==self.rear:
            value=self.front
            self.front=self.rear=None
            return value
        else:
            value=self.front
            self.front=self.front.next
            self.rear.next=self.front
            return value
            
    def display(self,q):
        temp=q.front
        print('Elements in circular queue are')
        while temp.next!=q.front:
            print(temp.data)
            temp=temp.next
        print(temp.data)
        
if __name__=="__main__":
    q=Queue()
    q.front=q.rear=None
    q.enQueue(2)
    q.enQueue(14) 
    q.enQueue(22) 
    q.enQueue(5) 
    result=q.deQueue()
    print('dequed obtained is',result.data)
    q.display(q)     
    
    
            
        
            
        