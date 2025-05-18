from cs50 import get_int

class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0
    def __str__(self):
        cookie = "🍪" * self.size
        return cookie

    def deposit(self, n):
        if self._size + n > self._capacity:
            print("jar has not enough capacity")
        else:
            self._size += n

    def withdraw(self, n):
        if self._size - n < 0:
            print("Not enough Cookie left")
        else:
            self._size -= n

    @property
    def capacity(self):
        if self._capacity < 0:
            print("Your jar is wrong")
        else:
            return self._capacity

    @property
    def size(self):
        return self._size

def main():

    jar = Jar()
    print("0 cookie in the jar")

    while (True):
        answer = get_int("Hungry? ")
        if answer == 100:
            break

        if answer > 0:
            jar.deposit(answer)
            print(str(jar))

        if answer < 0:
            jar.withdraw(-answer)
            print(str(jar))

main()