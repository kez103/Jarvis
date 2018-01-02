def sum(a, b):
    return a, b, a+b


if __name__ == '__main__':
    a, b, c = sum(1, 2)
    print(str(a) + " + " + str(b) + " = " + str(c))
