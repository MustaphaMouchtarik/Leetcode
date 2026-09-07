class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=Counter(nums)
        arr=[[] for i in range(len(nums)+1)]
        for key, val in dic.items():
            arr[val].append(key)
        res=[]
        for i in range(len(nums),0,-1):
            for num in arr[i]:
                res.append(num)
                if len(res)==k:
                    return res