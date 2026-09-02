class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []

        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        pairs = self.map.get(key, [])
        l = 0
        r = len(pairs) - 1

        while l <= r:
            m = (l + r) // 2

            if pairs[m][1] == timestamp:
                return pairs[m][0]
            elif pairs[m][1] < timestamp:
                ans = pairs[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return ans
