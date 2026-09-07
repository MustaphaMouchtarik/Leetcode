class Solution(object):
    def isValid(self, s):
        arr = list(s)
        for i in range(len(arr)):
            if arr[i] == "[":
                arr[i] = 1
            elif arr[i] == "]":
                arr[i] = -1
            elif arr[i] == "(":
                arr[i] = 2
            elif arr[i] == ")":
                arr[i] = -2
            elif arr[i] == "{":
                arr[i] = 3
            elif arr[i] == "}":
                arr[i] = -3
            else:
                return False
        changed = True
        while changed:
            changed = False
            i = 0
            while i < len(arr) - 1:
                if arr[i] > 0 and arr[i] == -arr[i + 1]:
                    del arr[i:i+2]
                    changed = True
                    break 
                i += 1

        return len(arr) == 0
