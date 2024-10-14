class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        cons_length = []
        nums_size = len(nums)
        if nums_size == 0:
            return 0
        
        temp_length = 1
        for i in range(1,nums_size):
            if nums[i] == nums[i-1] + 1:
                temp_length += 1
            else:
                cons_length.append(temp_length)
                temp_length = 1
        
        cons_length.append(temp_length)
        return max(cons_length)