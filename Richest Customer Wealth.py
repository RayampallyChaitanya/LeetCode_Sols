class Solution:
    def maximumWealth(accounts):
        max_num = []
        sum_list = 0
        for acc in accounts:
            for num in acc:
                sum_list = sum_list + num
            max_num.append(sum_list)
            sum_list = 0
        return max(max_num)


Solution.maximumWealth([[1,5],[7,3],[3,5]])