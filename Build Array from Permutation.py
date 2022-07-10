class Solution:
    def buildArray(nums):
        new_lst = []
        for num in nums:
            new_lst.append(nums[num])

        print(new_lst)


Solution.buildArray(nums=[0, 2, 1, 5, 3, 4])
