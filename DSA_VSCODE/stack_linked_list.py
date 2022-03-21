class Node:
    def __init__(self,value=None):
        self.value = value
        self.next =next

class LinkedList:
    def __init__(self):
        self.head = None        

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Stack:
    def __init__(self):
        self.LinkedList= LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values) 

    def isEmpty(self):
        if self.LinkedList.head ==None:
            return True
        else:
            return False    

    def push(self,value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head=node

    def pop(self):
        if self.isEmpty():
            return 'Stack is empty'
        else:
           nodeValue = self.LinkedList.head.value
           self.LinkedList.head = self.LinkedList.head.next
           return nodeValue        
    
    def delete(self):
        self.LinkedList.head = None

c_stack = Stack()
for i in range(5):
    c_stack.push(i)
print(c_stack.__str__())   
print('------')
c_stack.pop()
c_stack.pop()
print(c_stack.__str__()) 
# print(c_stack.isEmpty())

    