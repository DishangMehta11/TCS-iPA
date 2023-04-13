def isUNO(number: str) -> bool:
    # count = 1
    while len(number) > 1:
        total = 0
        for ch in number:
            total += int(ch)
        # count += 1
        number = str(total)
    return number == '1'


if __name__ == '__main__':
    print(isUNO(input()))