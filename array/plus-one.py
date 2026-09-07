class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        single = int("".join(map(str, digits))) +1
        return [int(x) for x in str(single)]