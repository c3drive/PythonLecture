class MyIterator:

    def __init__(self, start=0):
        self.current = start


    def __next__(self):
        num = self.current
        self.current += 1
        return num


    def __iter__(self):
        return self


# challenge
class EvenIteraror:

    def __init__(self, start):
        self.current = start


    def __next__(self):
        if self.current < 2:
            # yieldが最後まで行ってしまったときの例外を定義
            raise StopIteration
        else:
            if self.current % 2 == 0:
                num = self.current
                self.current -= 2
                return num
            else:
                self.current -= 1
                return self.__next__(self.current)


    def __iter__(self):
        return self


if __name__ == "__main__":
    myiterator = MyIterator(10)
    print(next(myiterator))
    print(next(myiterator))
    print(iter(myiterator))
    print(id(myiterator))
    print(id(iter(myiterator)))

    eveniterator = EvenIteraror(10)
    print(next(eveniterator))
    print(next(eveniterator))

    print(iter(eveniterator))
    print(id(iter(eveniterator)))
    print(id(eveniterator))
