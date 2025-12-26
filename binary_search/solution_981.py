class TimeMap:

    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = {}

        self.mp[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        m = self.mp[key]

        keyArr = list(m.keys())
        keyArr.sort()
        l, r = 0, len(keyArr) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if keyArr[mid] == timestamp:
                return m[keyArr[mid]]
            if keyArr[mid] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        if r >= len(keyArr):
            return m[keyArr[-1]]
        return m[keyArr[r]] if keyArr[r] <= timestamp else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
timeMap = TimeMap();
# timeMap.set("foo", "bar", 1);  # 存储键 "foo" 和值 "bar" ，时间戳 timestamp = 1
# print(timeMap.get("foo", 1))  # 返回 "bar"
# print(timeMap.get("foo", 3))  # 返回 "bar", 因为在时间戳 3 和时间戳 2 处没有对应 "foo" 的值，所以唯一的值位于时间戳 1 处（即 "bar"） 。
# timeMap.set("foo", "bar2", 4);  # 存储键 "foo" 和值 "bar2" ，时间戳 timestamp = 4
# print(timeMap.get("foo", 4))  # 返回 "bar2"
# print(timeMap.get("foo", 5))  # 返回 "bar2"
# ["TimeMap", "set", "set", "get", "get", "get", "get", "get"]
# [[], ["love", "high", 10], ["love", "low", 20], ["love", 5], ["love", 10], ["love", 15], ["love", 20], ["love", 25]]

timeMap.set('love', "high", 10)
timeMap.set("love", "low", 20)
print(timeMap.get("love", 5))
print(timeMap.get('love', 10))
print(timeMap.get('love', 15))
print(timeMap.get("love", 20))
print(timeMap.get("love", 25))
