class stack(list):
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, data):
        self.stack.append(data)
        self.size += 1

    def find(self, data):
        for i in range(self.size):
            if self.stack[i] == data:
                return i
        return False

    def pop(self):
        if self.is_empty():
            return -1
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def clear(self):
        self.stack.clear()
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        return f"[{', '.join(list(map(str, self.stack)))}]"


if __name__ == "__main__":
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.peek())
    print(s.pop())
    print(s.pop())