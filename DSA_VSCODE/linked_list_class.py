from random import randint

class LinkedList(object):
    def __init__(self):
        self.head=None
       
    def insert_after(self,val,pos):
        node = Node(val)
        ptr=self.head
        pre_ptr=ptr
        while ptr.val!=pos:
            pre_ptr=ptr
            ptr=ptr.next
        node.next = ptr.next
        ptr.next = node
       
    def insert_before(self,val,pos):
        node = Node(val)
        ptr = self.head
        pre_ptr = ptr
        if pos == self.head.val:
            node.next = self.head
            self.head = node
        else:
            while ptr.val != pos:
                pre_ptr = ptr
                ptr = ptr.next
            node.next = ptr
            pre_ptr.next = node
            
    # def delete_node(self,val):
    #     ptr = self.head
    #     pre_ptr=ptr
    #     if val!=None:
    #         if ptr.val==val:
    #             ptr=ptr.next
    #             pre_ptr=ptr
    #         else:
    #             while ptr.val!=val:
    #                 pre_ptr = ptr
    #                 ptr=ptr.next
    #             pre_ptr.next =ptr.next
    #             ptr=None
            
    def printData(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next
        
    # def generate(self,n,min_value,max_value):
    #     self.head=None    
    #     self.tail=None    
    #     for i in range(n):
    #         self.add(randint(min_value,max_value))
    #     return self

class  Node(object):
    def __init__(self,val):
        self.val=val
        self.next=None
        
if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next=second
    second.next = third
#     llist.insert_after(8,3)
#     llist.insert_before(8,1)
    # llist.delete_node(8)
    llist.printData()