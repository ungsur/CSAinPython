class Stack:
    def __init__(self):
        self._container = []

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.pop()

    def __repr__(self):
        return repr(self._container)

def main():
    num_discs = 3
    tower_a = Stack()
    tower_b = Stack()
    tower_c = Stack()
    tower_d = Stack()
    for i in range(1, num_discs + 1):
        tower_a.push(i)
    print(tower_a)


if __name__ == '__main__':
    main()