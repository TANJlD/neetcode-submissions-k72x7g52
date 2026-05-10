class TimeMap:

    def __init__(self):
        self.history = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.history[key].append([value, timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.history.get(key) # [[v, t], [v, t]]

        if not values or timestamp < values[0][1]:
            return ""

        l = 0
        r = len(values) - 1

        prev = 0

        while l <= r:
            m = (l+r) // 2
            if values[m][1] < timestamp:
                l = m + 1
                prev = max(prev, m)
            elif values[m][1] > timestamp:
                r = m - 1
            else:
                return values[m][0]

        return values[prev][0]




        
        
