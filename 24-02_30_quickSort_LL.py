#User function Template for python3

def parition(pivot,head):
    p=head
    ll=Llist()
    
    while p!=pivot:
        if p.data>pivot.data:
            pivot.next=p
            p.next=None
            p=ll.self.tail
         
            
def quickSortRecur():
     
    

def quickSort(head):
    #return head after sorting
    ptr=head
    pivot=head
    while ptr.next!=None:
        ptr=ptr.next
        pivot=ptr
    partition(pivot,head)    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
from collections import defaultdict
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        
def nodeID(head,dic):
    while head:
        dic[head.data].append(id(head))
        head=head.next
        


def printList(head,dic):
    while head:
        if id(head) not in dic[head.data]:
            print("Do'nt swap data, swap pointer/node")
            return
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        n=int(input())
        
        arr=[int(x) for x in input().split()]
        
        ll=Llist()
        tail=None
        
        for nodeData in arr:
            tail=ll.insert(nodeData,tail)
            
        dic=defaultdict(list)   # dictonary to keep data and id of node
        nodeID(ll.head,dic)     # putting data and its id
        
        resHead=quickSort(ll.head)
        printList(resHead,dic)  #verifying and printing
        print()
        
    
    
# } Driver Code Ends