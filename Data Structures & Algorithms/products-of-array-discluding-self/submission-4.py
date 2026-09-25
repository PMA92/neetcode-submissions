class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [0] * length
        prefix[0] = nums[0]

        suffix = [0] * length
        suffix[length - 1] = nums[length - 1]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]

        output = [0] * length
        output[-1] = prefix[-2]
        output[0] = suffix[1]
        for i in range(1, len(nums) - 1):
            output[i] = (int(suffix[i + 1] * prefix[i - 1]))
        return output