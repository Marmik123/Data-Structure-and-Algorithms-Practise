class Solution:
    def count(self, head, search_for):
        # Code here
        ptr=head
        count=0
        while (ptr is not None):
            if ptr.data==search_for:
                count+=1
            ptr=ptr.next
                
        return count  