class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        print(nums)
        count = 1
        best = 0
        pointer = 0
        subP = 0
        while pointer < len(nums) - 1:
            while ((subP < len(nums) - 1) and (nums[subP] + 1 == nums[subP + 1] or nums[subP] == nums[subP + 1])):
                if nums[subP] == nums[subP + 1]:
                    subP += 1
                    continue
                count += 1
                subP += 1
            best = max(best, count)
            count = 1
            if subP != pointer:
                pointer = subP
            else:
                pointer += 1
                subP = pointer
        return max(best, count)