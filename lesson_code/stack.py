class Stack():
    def __init__(self, *args):
        # self.stack_items = [arg for arg in args]
        self.stack_items = [*args]

    def peek(self):
        return self.stack_items[-1]

    def push(self, *args):
        for arg in args:
            self.stack_items.append(arg)

    def pop(self):
        return self.stack_items.pop()

    def size(self):
        return len(self.stack_items)

    def __str__(self):
        return str(self.stack_items)

    def __len__(self):
        return len(self.stack_items)


if __name__ == "__main__":
    test = Stack(1, 2, 3, 5)
    print(f"peek={test.peek()}")
    test.push(9)
    print("push 9後,Stack=", test)
    test.pop()
    print("pop後,Stack=", test)
    print("len = ", len(test))
