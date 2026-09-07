class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n ==2 :
            return "11"
        else:
            string="11"
            for i in range(3,n+1):
                c=1
                new=""
                for j in range(len(string)):
                    if j<len(string)-1:
                        if string[j]==string[j+1]:
                            c+=1
                        else:
                            new+=str(c)
                            c=1
                            new+=string[j]
                    else:
                        new+=str(c)
                        new+=string[j]
                string=new
        return string      
                
            
            
            
            
            
            
            