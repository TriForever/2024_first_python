class StackNode():
    def __init(self, data, next=None):
        self.data = data
        self.next = next


class LinkedStack():
    def __init__(self):
        self.top = None

    def push(self, data):
        current = StackNode(data)
        current.next = self.top
        self.top = current

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    def pop(self):
        if self.top:
            current = self.top
            self.top = current.next
            return current.data
        else:
            return None

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self):
        return_str = ""
        current = self.top
        while current:
            return_str += str(current.data)
            current = current.next

    if __name__ == "__main__":
