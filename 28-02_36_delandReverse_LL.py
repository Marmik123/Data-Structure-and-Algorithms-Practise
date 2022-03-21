#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

# Function to delete a given node from the list 
def deleteNode(head, key):
    #your code goes here
    curr=head
    prev=head
    # if curr.data==key and curr.next==head:
    #     head=None
    # else:
    while curr.data!=key:
        prev=curr
        curr=curr.next
    prev.next=curr.next
    curr=None
     
#Function to reverse the list
def reverseList(head):
    #your code goes here
    curr=head
    prev=head
    first=head
    last=head
    while curr.next!=head:
        curr=curr.next
    last=curr
    prev=last
    
    while first.next!=head:
        second=first.next
        first.next=prev
        prev=first
        first=second
    head=first
    first.next=prev
    # printList(head)
    
      
#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def push(data, prev):
    if prev == None:
        prev = Node(data)
        return prev
    tmp = Node(data)
    prev.next = tmp
    return tmp

def printList(head):
    flg = False
    tmp = head
    while flg== False or tmp!=head:
        flg = True
        print(tmp.data, end=" ")
        tmp = tmp.next
    print()

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(i) for i in input().split()]
        delNode = int(input())

        head = Node(None)
        prev = head
        for i in arr:
            prev = push(i, prev)
        head = head.next
        prev.next = head
        deleteNode(head, delNode)
        reverseList(head)
        printList(head)

# } Driver Code Ends