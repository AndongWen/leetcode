'''318最大单词长度成绩:
	给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。
'''
'''本题主要问题是判断两个字符串是否含相同字符，由于字符串只含有小写字符，总共 26 位，因此可以用一个 32 位的整数来存储每个字符是否出现过。'''
'''将ASCII字符转换为对应的数值即‘a’-->65，使用ord函数,ord('a')


反正，使用chr函数，将数值转换为对应的ASCII字符，chr(65)'''

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ret = [0] * len(words)
        for i in range(len(words)):
            for j in words[i]:
                ret[i] |=1 << (ord(j)-ord('a'))
            
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if ret[i]&ret[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
              
        return res
