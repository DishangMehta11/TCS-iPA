def checkLen(string: str) -> bool:
    for i in range(len(string)):
        if string[i].isdigit() and len(string[:i]) == int(string[i:]):
            return True
        # else:
    return False


if __name__ == '__main__':
    print(checkLen(input()))