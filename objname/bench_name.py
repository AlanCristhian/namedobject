import name
import time


def single_assignment():
    start = time.monotonic()
    for i in range(100_000):
        a = name.AutoName()
        b = name.AutoName()
        c = name.AutoName()
    end = time.monotonic()
    print(f"single_assignment {end - start:0.4g} seconds")


def unpack_sequence():
    start = time.monotonic()
    for i in range(100_000):
        a, b, c = name.AutoName()
    end = time.monotonic()
    print(f"unpack_sequence {end - start:0.4g} seconds")


if __name__ == '__main__':
    single_assignment()
    unpack_sequence()
