class Solution(object):
    def twoSum(self, nums, target):
        k = {}
        a = []
        for i, val in enumerate(nums):
            if target - val in k:
                a.append(i)
                a.append(k[target - val])
                return a
            k[val] = i

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
