def add(a, b):
    return a + b


def subtract(a, b):
    unused_variable = 123
    return a - b


if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
