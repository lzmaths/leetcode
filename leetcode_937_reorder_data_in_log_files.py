import sys

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        if not logs:
            return []
        letter_logs = []
        digit_logs = []
        for log in logs:
            idx = log.find(" ")
            identifier, content = log[:idx], log[idx+1:]
            if content[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append([identifier, content])
                
                
        letter_logs.sort(key=lambda x: (x[1], x[0]))
        ans = []
        for identifier, content in letter_logs:
            ans.append(identifier+ " " + content)
            
        return ans + digit_logs