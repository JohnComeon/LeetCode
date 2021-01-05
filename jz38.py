class Solution:
    def permutation(self, s):
        res = []
        c = list(s)
        n = len(c)
        def traceback(x):
            if x==n-1:
                res.append(''.join(c))
                return
            dic = set()
            for i in range(x, n):
                if c[i] in dic:     # 重复 ， 需要剪枝
                    continue
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]  # 交换，将 c[i] 固定在第 x 位
                traceback(x+1)
                c[i], c[x] = c[x], c[i]  # 恢复交换
        traceback(0)
        return res

s = "aab"
c = Solution()
res = c.permutation(s)
print(res)
