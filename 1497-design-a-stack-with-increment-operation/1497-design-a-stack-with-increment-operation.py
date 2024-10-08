class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
          
        

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1
        

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            for i in range(0, len(self.stack)):
                if i < k:
                    self.stack[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)