class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # myDict = {}
        # for num in nums:
        #     if num in myDict:
        #         return True 
        #     myDict[num] = num
        # return False

        #Brute Force
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True 
        return False