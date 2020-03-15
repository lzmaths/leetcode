import sys, collections

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ans = []
        dic = {word: idx for idx, word in enumerate(words)}
        for idx, word in enumerate(words):
            rword = word[::-1]
            if rword in dic and dic[rword] != idx:
                ans.append([idx, dic[rword]])

            for s in self.prefix(word):
                rs = s[::-1]
                if rs in dic and idx != dic[rs]:
                    ans.append([idx, dic[rs]])

            for s in self.suffix(word):
                rs = s[::-1]
                if rs in dic and idx != dic[rs]:
                    ans.append([dic[rs], idx])

        return ans

    def prefix(self, s):
        ans = []
        for i in range(len(s)):
            if s[i:] == s[i:][::-1]:
                ans.append(s[:i])
        return ans

    def suffix(self, s):
        ans = []
        for i in range(len(s)):
            if s[:i+1] == s[:i+1][::-1]:
                ans.append(s[i+1:])
        return ans
        

        