from functions import square


def announce(f):
    def wrapper():
        print(F"About to run the function...")
        f()
        print("Done...")

    return wrapper()


@announce
def range_square():
    for i in range(10):
        print(f"The square of {i} is {square(i)}")