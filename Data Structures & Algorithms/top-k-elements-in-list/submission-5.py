class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen_k = defaultdict(int)
        topKL  = []
        for num in nums:
            seen_k[num] += 1

        while len(topKL) != k:
            max_k = max(seen_k, key=seen_k.get)
            topKL.append(max_k)
            seen_k.pop(max_k)
        return topKL
