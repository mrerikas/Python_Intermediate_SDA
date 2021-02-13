from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add_record(self, record):
        pass

    @abstractmethod
    def __contains__(self, item):
        pass

    @abstractmethod
    def index(self, value):
        pass


class DictStorage(dict, Storage):
    length = 0

    def index(self, value):
        if value in self:
            return self[value][0]
        else:
            raise ValueError(f"{value} not in DictStorage")

    def rindex(self, value):
        if value in self:
            return self[value][-1]
        else:
            raise ValueError(f"{value} not in DictStorage")

    def indexes(self, value):
        if value in self:
            return self[value]
        else:
            raise ValueError(f"{value} not in DictStorage")

    def add_record(self, record):
        i = self.length
        self[record] = self.get(record, []) + [i]
        self.length += 1

    def __getitem__(self, item):
        print("OK")
        return super().__getitem__(item)


class ListStorage(list, Storage):
    def add_record(self, record):
        self.append(record)


ds = DictStorage()
ds.add_record("8")
ds.add_record(5)
ds.add_record(1)
ds.add_record("8")
ds.add_record(5)
ds.add_record(1)
ds.add_record("8")
ds.add_record(5)
ds.add_record(1)
if __name__ == '__main__':
    print(ds["8"])
