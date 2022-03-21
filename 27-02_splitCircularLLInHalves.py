#User function Template for python3

'''
class Node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def splitList(self, head, head1, head2):
        #code here
        slow=head
        fast=head
        
        if head==None:
            return
        else:
            
            while fast.next!=head and fast.next.next!=head:
                fast=fast.next.next
                slow=slow.next
            head1=head
        
        #CHECKNG IF THERE ARE EVEN ELEMENTS.
            if fast.next.next==head:
                fast=fast.next
            head2=slow.next
            
            fast.next=slow.next
            slow.next=head
        
        #this is to emulate pass by reference in python please don't delete below line.
            return head1,head2

#{ 
#  Driver Code Starts
#Initial Template for Python 3


class Node:
    def __init__(self):
        self.data = None
        self.next = None

def printCircularLinkedList(head):
    tmp = head
    while True:
        print(tmp.data, end = " ")
        tmp = tmp.next
        if tmp == head:
            break
    print()
    
if __name__ == "__main__":
    for i in range(int(input())):
        head = Node()
        head1 = Node()
        head2 = Node()
        tmp = head
        n = int(input())
        for i in input().split():
            tmp.next = Node()
            tmp = tmp.next
            tmp.data = int(i)
        head = head.next
        tmp.next = head
        obj = Solution()
        head1,head2 = obj.splitList(head,head1,head2)
        printCircularLinkedList(head1)
        printCircularLinkedList(head2)


# } Driver Code Ends