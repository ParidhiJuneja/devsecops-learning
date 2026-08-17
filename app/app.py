def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def square(a):
    return a * a


def is_even(a):
    return a % 2 == 0


if __name__ == "__main__":
    print("V2 - 2 + 3 =", add(2, 3))
    print("V2 - 5 - 2 =", subtract(5, 2))
