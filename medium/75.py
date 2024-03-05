class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = [], [], []
        for i in range(len(nums)):
            if nums[i] == 0: red.append(0)
            if nums[i] == 1: white.append(1)
            if nums[i] == 2: blue.append(2)
        nums.clear()
        nums.extend(red)
        nums.extend(white)
        nums.extend(blue)
        return nums
