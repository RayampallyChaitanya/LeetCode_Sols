class Solution:
    def getConcatenation(nums):
        new_list = []
        for i in range(2):
            for num in nums:
                new_list.append(num)

        print(new_list)


Solution.getConcatenation(nums=[1,2,1])

