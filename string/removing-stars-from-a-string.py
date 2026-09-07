class Solution:
    def removeStars(self, s: str) -> str:
        deque=[]
        for char in s:
            if char=="*":
                deque.pop()
            else:
                deque.append(char)
        return "".join(deque)