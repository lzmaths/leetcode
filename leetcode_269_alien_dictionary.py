import sys, collections

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        pre, suc = collections.defaultdict(set), collections.defaultdict(set)
        for pair in zip(words, words[1:]):
            for a, b in zip(pair[0], pair[1]):
                if a != b:
                    suc[a].add(b)
                    pre[b].add(a)
                    break
        
        ans = ''
        chars = set("".join(words))
        cands = chars - set(pre.keys())
        while cands:
            ch = cands.pop()
            ans += ch
            for item in suc[ch]:
                pre[item].discard(ch)
                if not pre[item]:
                    cands.add(item)
                
        return ans if len(chars) == len(ans) else ""
        