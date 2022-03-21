# num = int(input("Enter a Number "))
# find = 50

def find_number(num, find):
    result = ""
    if num == find:
        result = "Hourra !"
    elif (find - 10) <= num <= (find + 10):
        result = "almost"
    if num < find - 10:
        result = "to small"
    elif num > find + 10:
        result = "To big"
    print(result)


def square(x):
    return x * x
