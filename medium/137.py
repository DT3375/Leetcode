class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else: 
                count[nums[i]] += 1
        for key, value in count.items():
            if value == 1:
                return key
