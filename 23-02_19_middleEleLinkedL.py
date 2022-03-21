# your task is to complete this function

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''
def getCount(head_node):
    
    count=0    
    ptr=head_node
    if ptr.next==None:
        return 1
    else:
        while ptr:
            count+=1
            ptr=ptr.next
        return count
            
class Solution:

    # Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        length=getCount(head)
        mid=length//2 + 1
        
        if mid==1:
            return head.data
        else:
            i=1
            ptr=head
            while i<mid:
                i+=1
                ptr=ptr.next
            return ptr.data    
                
                

#{ 
#  Driver Code Starts
# Initial Template for Python3

# Node Class    
class node:
    def __init__(self):
        self.data = None
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.tail = self.head
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next

def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print('')

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        ob = Solution()
        print(ob.findMid(list1.head))


# } Driver Code Ends