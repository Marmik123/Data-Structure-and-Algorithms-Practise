
# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        split_words=S.split(".")
        # print(split_words)
        i=0
        j=len(split_words)-1
        str=''
        while i<j:
            temp=split_words[i]
            split_words[i]=split_words[j]
            split_words[j]=temp
            i+=1
            j-=1
        for x in range(len(split_words)):
            str+=split_words[x]
            if x!=len(split_words)-1:
                str=str+'.'
        return str   
        
            
            
            # if x==len(split_words)-1:
            #     break
            # else:
                
                
        print(str)
        # for 
            
        
#{ 
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends