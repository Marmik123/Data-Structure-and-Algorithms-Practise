class Queue:
    def __init__(self):
        self.elements =[]

    def __str__(self):
        values = [str(x) for x in self.elements]
        return ''.join(values)

    def isEmpty(self):
        if self.elements==[]:
            return True
        else:
            return False

    def enqueue(self,value=None):
        self.elements.append(value)
        return 'Element inserted at the end of queue'    

    def dequeue(self):
        if self.isEmpty(): 
            return 'Queue is empty'
        else:
            return self.elements.pop(0)    
    
    def peek(self):
        if self.isEmpty():
            return 'Queue is empty'
        else:
            return self.elements[0]    

    def delete(self):
        self.elements=None

#CIRCULAR QUEUE
class CircQueue:
    def __init__(self,maxSize):
        self.elements = [None]*maxSize
        self.maxSize=maxSize
        self.start=-1
        self.top=-1

    def __str__(self):
        values = [str(x) for x in self.elements]
        return ' '.join(values)

    def enqueue(self,value=None):
        if self.isFull():
            return 'Queue is full'
        else:
            if self.top +1 == self.maxSize:
                self.top=0
            else:
                self.top+=1
                if self.start==-1:
                    self.start=0

            self.elements[self.top] = value    
            return 'element inserted successfully at the end'

    def dequeue(self):
        if self.isEmpty():
            return 'Queue is already empty'

        else:
            firstEle = self.elements[self.start]
            start = self.start
            if self.start==self.top:
                self.start=-1
                self.top=-1
            elif self.start+1==self.maxSize:
                self.start=0
            else:
                self.start+=1
            self.elements[start]=None
            return firstEle        
  
    def peek(self):
        if self.isEmpty():
            return 'Queue is empty'
        else:
            self.elements[self.start]

    def isFull(self):
        if self.start==0 and self.top==self.maxSize-1:
            return True
        elif self.top + 1 == self.start:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False    

                            
# queue = Queue()
# for i in range(3):
#     queue.enqueue(i+1)

# print(queue.isEmpty())
# print('--------')
# print(queue.__str__())
# print(queue.dequeue())
# print(queue.__str__())
# print(queue.peek())

# circQ = CircQueue(6)
# circQ.enqueue(1)
# circQ.enqueue(2)
# print(circQ.enqueue(3))
# print(circQ.__str__())
# print(circQ.dequeue())
# print(circQ.peek())
# print(circQ.__str__())

#QUEUE USING LINKED LIST
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next = None

    def __str__(self):
        return str(self.value)    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
        return curNode    

class QueueLL:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    def enqueue(self,value):
        newNode = Node(value)
        if self.linkedList.head==None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty'
        else:
            temp = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return temp  

    def delete(self):
        self.linkedList.head=None
        self.linkedList.tail=None          
                            

llqueue = QueueLL()
llqueue.enqueue(1)
llqueue.enqueue(2)
llqueue.enqueue(3)
print('LIST')
print(llqueue.__str__())
llqueue.dequeue()
llqueue.dequeue()
llqueue.dequeue()
llqueue.dequeue()

print('LIST AFTER DEQUEUE')
print(llqueue.__str__())

               