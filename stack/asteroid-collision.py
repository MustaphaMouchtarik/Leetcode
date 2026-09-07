class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        stack=[]
        for i in range(len(ast)):
            v=True
            if len(stack)==0:
                stack.append(ast[i])
            else:
                while stack and ast[i]<0 and stack[-1]>0: #colision
                    if -ast[i]>stack[-1]:
                        stack.pop()
                    elif -ast[i]==stack[-1]:
                        stack.pop()
                        v=False
                        break
                    else:
                        v=False
                        break
                if v:
                    stack.append(ast[i])
        return stack




        
