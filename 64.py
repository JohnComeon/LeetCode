class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n: int) -> int:
        n>1 and self.sumNums(n-1)
        self.res += n       # 回溯
        return self.res

solution = Solution()
res = solution.sumNums(3)
print(res)
