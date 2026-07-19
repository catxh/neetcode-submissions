from collections import deque

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums = deque(nums)    
        k_list = []

        while len(k_list) != k:
            k_list.append(nums.popleft())
        for num in nums:
            if num > min(k_list):
                k_list.remove(min(k_list))
                k_list.append(num)
        return min(k_list)
