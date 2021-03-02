#Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_length = len(nums)
        final_list = []
        i = 0
        j = 1
        while i < nums_length:
            while j < nums_length:
                if nums[i] + nums[j] == target:
                    final_list.append(i)
                    final_list.append(j)
                    break;
                j = j+1
            i = i+1
        return final_list

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in seen:
                return [seen[remaining], i]
            seen[num] = i
        return []

