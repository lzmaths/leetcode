class LogSystem(object):

    # timestamp format: "2017:01:01:23:59:59"
    def __init__(self):
        self.m = {'Year':4, 'Month':7, "Day":10, 'Hour':13, "Minute":16, "Second":19}
        self.log = []

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: None
        """
        self.log.append((id, timestamp))
        

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        res = []
        for unit in self.log:
            ts = unit[1]
            if s[:self.m[gra]] <= ts[:self.m[gra]] <= e[:self.m[gra]]:
                res.append(unit[0])

        return res

        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)