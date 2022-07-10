class Solution:
    def finalValueAfterOperations(operations):
        X = 0
        dic = {'--X':'sub','X--':'sub','X++':'add','++X':'add'}
        for oper in  operations:
            if dic[oper] == 'sub':
                X = X - 1
            elif dic[oper] == 'add':
                X = X + 1

        print(X)


Solution.finalValueAfterOperations(["++X","++X","X++"])
