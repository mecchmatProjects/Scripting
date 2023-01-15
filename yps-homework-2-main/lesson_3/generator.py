#!venv/bin/python


class SqrtIterator:
    """Paired numbers iterator"""

    def __init__(self, end: int = 0):
        self._counter = 0
        self._end = end

    def __iter__(self):
        """must-have method"""
        print("It's time to __iter__")
        self._counter = 0
        return self

    def __next__(self):
        """must-have method"""
        if self._counter >= self._end:
            print("I'm tired. Time to stop")
            raise StopIteration

        self._counter += 1
        value = self._counter * self._counter
        print(f"New value from __nest__ is {value}")
        return value


if __name__ == "__main__":
    print("Start is here")
    iterator = SqrtIterator(10)
    print("Generate list")
    list_from_iterator = [i for i in iterator]
    print(list_from_iterator)
