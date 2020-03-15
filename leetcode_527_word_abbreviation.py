import collections

class Solution(object):
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        abb = collections.defaultdict(int)
        for i, word in enumerate(dict):
            for j in range(1, len(word)-2):
                abb[word[:j] + str(len(word) - j - 1) +word[-1]] += 1

        for i, word in enumerate(dict):
            for j in range(1, len(word)-2):
                curr = word[:j] + str(len(word) - j - 1) +word[-1]
                if abb[curr] == 1:
                    dict[i] = curr
                    break

        return dict

solution = Solution()
dic = ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
print(solution.wordsAbbreviation(dic))
