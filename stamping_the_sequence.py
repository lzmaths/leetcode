class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        stamp_len, target_len = len(stamp), len(target)
        total = 0
        seen = [False] * target_len
        ans = []
        while total < target_len:
            flag = False
            for i in range(target_len - stamp_len + 1):
                if seen[i]:
                    continue
                matched_len = self.check(stamp, target, i)
                if matched_len == 0:
                    continue
                seen[i] = True
                total += matched_len
                ans.append(i)
                flag = True
            if not flag:
                break
        return ans[::-1]
                
        
        
    def check(self, stamp, target, k):
        stamp_len, target_len = len(stamp), len(target)
        matched_len = stamp_len
        for i in range(stamp_len):
            if target[i+k] == '?':
                matched_len -= 1
            elif stamp[i] != target[i+k]:
                return 0
        
        if matched_len != 0:
            for i in range(stamp_len):
                target[i+k] = '?'
        
        return matched_len
