from heapq import heapify, heappush, heappop


class PriorityQueue:
    def __init__(self):
        self.heap = []
        heapify(self.heap)

    def push(self, num):
        heappush(self.heap, num)

    def head(self):
        return self.heap[0]

    def elements(self):
        for num in self.heap:
            print(num, end=' ')

    def pop(self):
        return heappop(self.heap)


if __name__ == '__main__':
    p = PriorityQueue()
    for n in [5, 3, 17, 10, 84, 19, 6, 22, 9]:
        p.push(n)
    p.elements()
    print()
    print(p.pop())
    print(p.pop())
    print(p.pop())
    print(p.pop())
    print(p.pop())
    print(p.pop())
    print(p.pop())
    p.elements()
