class TimeMap:

    def __init__(self):
        self.store = {} #hash map - key=string, value=[list of [value, timestamp]]
        # key : list of [val, timestamp]


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])    


    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        # binary search
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            # check for valid values - if equal or less than time stamp can return it
            if values[m][1] <= timestamp:
                # closest weve seen so far
                res = values[m][0]
                l = m+ 1
            else:
                # val too big
                r = m - 1
        return res