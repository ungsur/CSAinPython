class Stack:
    def __init__(self):
        self._container = []

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.pop()

    def __repr__(self):
        return repr(self._container)


def hanoi(begin, end, temp, n):
    print("execution")
    if n == 1:
        end.push(begin.pop())
    else:     #123 0 0  3
        hanoi(begin, temp, end, n-1)    #123  0 0 2
        hanoi(begin, end, temp, 1)      #23 1 0 1
        hanoi(temp, end, begin, n-1)    #3 1


def main():
    num_discs = 3
    tower_a = Stack()
    tower_b = Stack()
    tower_c = Stack()
    for i in range(1,num_discs + 1):
        tower_a.push(i)
    print(tower_a)
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b) 
    print(tower_c)



if __name__ == '__main__':
    main()