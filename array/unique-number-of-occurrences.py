class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic=Counter(arr)
        return len(set(dic.values()))==len(list(dic.values()))