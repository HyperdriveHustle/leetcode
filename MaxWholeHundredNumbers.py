# -*- coding:utf-8 _*-

'''
深信服2019春招笔试题

题目描述：
输入是一个数组，找到从左上角到右下角的路径和最大且为整百的值，如果不存在整百的路径和，则返回-1

思路：
回溯法获得所有路径，如果符合要求则更新res值。
'''

class Solution(object):
    def __init__(self):
        self.res = -1
        self.pathValue = []

    def MaxWholeHundredNums(self, arr):
        width = len(arr[0])
        height = len(arr)

        def getPathValue(curSum, i, j):
            if i == height - 1 and j == width - 1:
                self.pathValue.append(curSum + arr[i][j])
                if (curSum + arr[i][j]) % 100 == 0 and curSum + arr[i][j] > self.res:
                    self.res = curSum + arr[i][j]
                return
            if i < height -1:
                getPathValue(curSum + arr[i][j], i + 1, j)
            if j < width - 1:
                getPathValue(curSum + arr[i][j], i, j+1)

        getPathValue(0, 0, 0)
        return self.res


if __name__ == '__main__':
    arr = list()
    arr1 = [[30,70,90,10,30], [40,80,30,20,40], [90,70,70,40,50], [20,90,90,90,90]]
    arr2 = [[30,40], [10,60]]
    arr3 = [[30, 50, 60], [20, 40, 70]]
    arr4 = [[800,800,800],[800,800,800],[800,800,800],[800,800,800]]

    sol = Solution()
    print sol.MaxWholeHundredNums(arr1)
    sol = Solution()
    print sol.MaxWholeHundredNums(arr2)
    sol = Solution()
    print sol.MaxWholeHundredNums(arr3)
    sol = Solution()
    print sol.MaxWholeHundredNums(arr4)