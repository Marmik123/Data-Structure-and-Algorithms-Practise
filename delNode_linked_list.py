# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def delNode(head, k):
    # Code here
    if head==None:
        return None
    elif k==1:
        ptr=head
        head=ptr.next
        ptr=None
        return head
    else:
        ptr=head
        pre_ptr=ptr
        i=1
        while i<k:
            pre_ptr=ptr
            ptr=ptr.next
            i+=1
        if ptr.next==None:
            pre_ptr.next=None
            
        else:
            pre_ptr.next=ptr.next
            ptr.next=None
        return head        
    
#{ 
#  Driver Code Starts
# Node Class    
class node:
    def __init__(self):
        self.data = None
        self.next = None
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

def printlist(head):
    temp = head
    while(temp):
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
        k = int(input())
        newhead = delNode(list1.head, k)
        printlist(newhead)
# Contributed By: Harshit Sidhwa
# } Driver Code Ends