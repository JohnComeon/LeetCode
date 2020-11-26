import collections
class Solution:
    def dicesProbability(self, n: int):
        dp = {}    # dp为当前点数之和：概率的字典
        dp[0] = 1
        for i in range(1, n+1):
            newdp = collections.defaultdict(int)    # 每次重新赋值
            for sm in dp:              # 前n-1个骰子的6个点数（1~6）
                for v in range(1,7):    # 新加的骰子的6个点数（1~6）
                    newdp[sm+v] += dp[sm] / 6    # sm+v即为最终的sum， 累加和
            dp = newdp
        res = []
        for sm in range(n, 6*n+1):  # n个骰子，点数最小之和为n，最大为6*n
            res.append(dp[sm])
        return res

s = Solution()
print(s.dicesProbability(2))
