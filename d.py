
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        s = list(s)
        if not s:
            return ''
        def revers(start, end)  :  # 字符串翻转函数
            low = start
            high = end
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            return (''.join(s[low:high +1])) + ' '

        length = len(s)
        revers(0, length -1)
        start = 0
        end = 0
        result = ''
        while end <= length:
            if s[start] == ' ':
                start += 1
                end += 1
            elif end == length or s[end] == ' ':
                print(start ,end)
                temp = revers(start, end -1 )  # 每次返回的是一个单词进行翻转完之后的结果,并且后面带有一个空格
                result = ''.join([result ,temp])  # 将结果连接在一起
                start = end +1
                end += 1
            else:
                end += 1
        return result[:-1  ]  # 因为最后有一个空格,所以要去除掉

s = "a good   example"
c = Solution()
res = c.reverseWords(s)
print(res)
