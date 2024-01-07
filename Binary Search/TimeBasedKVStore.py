class TimeMap:

    def __init__(self):
        self.mapper = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mapper:
            self.mapper[key].append((timestamp, value))
        else:
            self.mapper[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapper:
            return ""
        else:
            to_search = self.mapper[key]
            left = 0
            right = len(to_search) - 1
            while left < right:
                mid = left + (right - left) // 2
                if to_search[mid][0] == timestamp:
                    return to_search[mid][1]
                elif to_search[mid][0] < timestamp:
                    left = mid + 1
                else:
                    right = mid
            if to_search[left][0] <= timestamp:
                return to_search[left][1]
            elif left - 1 >= 0 and to_search[left - 1][0] <= timestamp:
                return to_search[left - 1][1]
            else:
                return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
