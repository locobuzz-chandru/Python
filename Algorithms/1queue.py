def queue_function1():
    queue_ = []
    for x in range(1, 6):
        queue_.append(x)
    for x in range(len(queue_)):
        queue_.pop(0)
    return queue_


def queue_function2():
    import collections
    queue_ = collections.deque()
    for x in range(1, 6):
        queue_.appendleft(x)
    for x in range(len(queue_)):
        queue_.pop()
    return queue_


def queue_function3():
    import queue
    queue_ = queue.Queue()
    for x in range(1, 6):
        queue_.put(x)
    for x in range(5):
        queue_.get()
    return queue_


if __name__ == '__main__':
    queue_function1()
    queue_function2()
    queue_function3()
