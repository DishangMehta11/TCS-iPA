def multi(string: str) -> int:
    mul = 1
    for ch in string:
        mul *= int(ch)

    return mul


if __name__ == '__main__':
    print(multi(input()))