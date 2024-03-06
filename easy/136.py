class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = []
        for i in range(len(nums)):
            if nums[i] not in single:
                single.append(nums[i])
            else: single.remove(nums[i])
        return single[0]
