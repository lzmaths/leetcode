import collections

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            val = self.cache[key]
            self.cache.move_to_end(key)
            return val

    def put(self, key: int, value: int) -> None:
        self.get(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)