class TimeMap:

    def __init__(self):
        self.store={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [] # need to make the key have an empty array to append our value and timestamp
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # binary search - return value (str) at our key and timestamp provided - can be <= timestamp but closest to timestamp
        res = ""
        values = self.store.get(key, []) # either get our values from this key as [["bar1",1],["bar2",5],["barN", n]] or make an empty list at that key []
        l = 0
        r = len(values)-1
        while l <= r:
            m = (l+r) // 2
            if values[m][1] <= timestamp:
                #any timestamp behind our sought timestamp is a valid string result
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
         