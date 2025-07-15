class MinStack:

    def __init__(self):
        self.lows = []
        self.curr = []

    def push(self, val: int) -> None:
        self.curr.append(val)
        
        if not self.lows:
            self.lows.append(val)

        elif len(self.lows) >= 1:
            if val >= self.lows[-1]:
                self.lows.append(self.lows[-1])
            else:
                self.lows.append(val)

    def pop(self) -> None:
        self.lows.pop()
        self.curr.pop()

    def top(self) -> int:
        return self.curr[-1]

    def getMin(self) -> int:
        return self.lows[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()