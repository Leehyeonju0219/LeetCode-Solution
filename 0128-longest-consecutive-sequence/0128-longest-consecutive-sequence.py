class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        max_length = 1
        nums_size = len(nums)
        if nums_size == 0:
            return 0
        
        temp_length = 1
        for i in range(1,nums_size):
            if nums[i] == nums[i-1] + 1:
                temp_length += 1
            else:
                max_length = max(temp_length, max_length)
                temp_length = 1
        
        return max(max_length, temp_length)