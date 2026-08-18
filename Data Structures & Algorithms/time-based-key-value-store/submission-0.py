class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        entries = self.store[key]
        low, high = 0, len(entries)
        while low < high:
            mid = (low + high) // 2
            if entries[mid][0] <= timestamp:
                low = mid + 1
            else:
                high = mid
        
        if low == 0:
            return ""
        return entries[low - 1][1]

        
