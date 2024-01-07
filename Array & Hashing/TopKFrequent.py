class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in nums:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        y = list(hash_map.items())
        y.sort(key=lambda x: x[1], reverse=True)
        return map(lambda x: x[0], y[0:k])
