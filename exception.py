def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Division by zero")


def main():
    print(divide(10, 2))
    print(divide(10, 0))


if __name__ == "__main__":
    main()
