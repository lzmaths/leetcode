import sys

class Horse(object):
    """
    given a string like: neineighghneigh, count the number of horses (neigh)
    """
    def countHorse(self, s):
        dic = {val: idx for idx, val in enumerate("neigh")}
        counts = [0, 0, 0, 0, 0]
        ans = 0
        for idx, ch in enumerate(s):
            counts[dic[ch]] += 1
            if ch == 'n':
                ans = max(ans, counts[0])
            else:
                if counts[dic[ch]-1] < counts[dic[ch]]:
                    return -1
                if ch == 'h':
                    counts = [num-1 for num in counts]
                    
        return -1 if max(counts) != 0 else ans

horse = Horse()
print(horse.countHorse("neineighghneigh")) # expect 2
print(horse.countHorse("neineighghneighn")) # expect -1
print(horse.countHorse("neineighghnigh")) # expect -1
