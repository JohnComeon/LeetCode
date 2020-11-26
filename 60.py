import collections
class Solution:
    def dicesProbability(self, n: int):
        dp = {}    # dp为当前点数之和：概率的字典
        dp[0] = 1
        for i in range(1, n+1):
            newdp = collections.defaultdict(int)
            for sm in dp:
                for v in range(1,7):
                    newdp[sm+v] += dp[sm] / 6
            dp = newdp
        res = []
        for sm in range(n, 6*n+1):  # n个骰子，点数最小之和为n，最大为6*n
            res.append(dp[sm])
        return res

s = Solution()
print(s.dicesProbability(2))
