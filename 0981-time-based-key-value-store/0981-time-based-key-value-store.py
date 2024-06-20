class TimeMap:

    def __init__(self):
        self.mapof_Map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.mapof_Map:
            self.mapof_Map[key] = [[value, timestamp]]
        else:
            self.mapof_Map[key].append([value, timestamp])
        


    def get(self, key: str, timestamp: int) -> str:
        target = timestamp
        if key not in self.mapof_Map:
            return ""
        else:
            l, r = 0, len(self.mapof_Map[key]) - 1
            res = ''
            mid = 0
            while(l <= r):
                mid = int((l+r)//2)
                if self.mapof_Map[key][mid][-1] > target:
                    r = mid - 1
                elif self.mapof_Map[key][mid][-1] <= target:
                    res = self.mapof_Map[key][mid][0]
                    l = mid + 1
                
            return res

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)