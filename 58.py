class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = list(s)
        length = len(s)

        def swap(start, end):  # 字符串翻转函数
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        swap(0, length - 1)
        i, j = 0, 0
        while j <= length:
            if s[i] == ' ':
                print(i)
                i += 1
                j += 1

            elif j == length or s[j] == ' ':  # 这个判断语句中的判断条件的前后顺序也很重要
                swap(i, j - 1)
                i = j + 1
                j += 1
            else:
                j += 1
        return ''.join(s)


s = "a good   example"
c = Solution()
res = c.reverseWords(s)
print(res)
