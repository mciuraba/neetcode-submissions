class MinStack:
    def __init__(self):
        self.arr = []
        self.mins = []

    def push(self, val: int) -> None:
        self.arr.append(val)

        if not self.mins:
            self.mins.append(val)
        else:
            self.mins.append(min(val, self.mins[-1]))

    def pop(self) -> None:
        self.arr.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.mins[-1]
