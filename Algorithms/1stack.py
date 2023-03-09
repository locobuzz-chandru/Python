def stack():
    stack_ = []
    for x in range(1, 6):
        stack_.append(x)
    for x in range(len(stack_)):
        stack_.pop()
    return stack_


def deque_stack():
    import collections
    stack_ = collections.deque()
    for x in range(1, 6):
        stack_.append(x)
    for x in range(len(stack_)):
        stack_.pop()
    return stack_


def queue_stack():
    import queue
    stack_ = queue.LifoQueue(5)
    for x in range(1, 6):
        stack_.put(x, timeout=1)
    for x in range(10):
        stack_.get(timeout=1)
    return stack_


if __name__ == '__main__':
    stack()
    deque_stack()
    queue_stack()
