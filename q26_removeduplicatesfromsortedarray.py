class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        
        if len(nums) == 1:
            return 1
        
        for j in range(1, len(nums)):
            if nums[i] != nums[j] and i + 1 != j:
                nums[i + 1], nums[j] = nums[j], nums[i + 1]
                i += 1
        
        return i + 1