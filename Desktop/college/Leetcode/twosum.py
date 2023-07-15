class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force
        # for num in range(len(nums)-1):
        #     for n in range(num+1, len(nums)):
        #         if nums[num] + nums[n] == target:
        #             return [num, n]
        nums_dict = {}
        nums_len = len(nums)
        # count = 0
        # for num in nums:
        #     dict[num] = count 
        #     count += 1
        for i in range(nums_len):
            nums_dict[nums[i]] = i
        for i in range(nums_len):
            complement = target - nums[i]
            #make sure the value of the complement is not itself
            if complement in nums_dict and nums_dict[complement] != i :
                return [i, nums_dict[complement]]