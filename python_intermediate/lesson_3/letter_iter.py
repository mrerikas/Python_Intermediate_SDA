class LetterIterator:
    def __init__(self, start, stop):
        self.start = ord(start) - 1
        self.stop = ord(stop)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start < self.stop:
            return self.start
        else:
            raise StopIteration()


if __name__ == '__main__':
    r = LetterIterator('a', 'z')
    for n in r:
        print(chr(n))

# ord('letter) - > parodo koda
# chr(numeris) - > pavercia kod ai raide
