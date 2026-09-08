class MyQueue:

    def __init__(self):
        self.front_stack = []
        self.back_stack = []

    def push(self, x: int) -> None:
        self.back_stack.append(x)

    def _transfer(self):
        if not self.front_stack:
            while self.back_stack:
                self.front_stack.append(self.back_stack.pop())

    def pop(self) -> int:
        self._transfer()
        return self.front_stack.pop()

    def peek(self) -> int:
        self._transfer()
        return self.front_stack[-1]

    def empty(self) -> bool:
        return not self.front_stack and not self.back_stack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()