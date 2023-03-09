def stack():
    stack_ = []
    for x in range(1, 6):
        stack_.append(x)
    for x in range(len(stack_)):
        stack_.pop()
    return stack_


if __name__ == '__main__':
    stack()
