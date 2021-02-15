class Range:
    def __init__(self, start, stop, step=1):
        self.start = start - step
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        if self.start < self.stop:
            return self.start
        else:
            raise StopIteration()


if __name__ == '__main__':
    r = Range(0, 8)
    for n in r:
        print(n)
