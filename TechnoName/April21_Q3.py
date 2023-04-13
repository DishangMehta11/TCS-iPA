def remove756(string: str) -> str:
    temp = ''
    i = 0
    while i < len(string):
        if string[i] == '7':
            i += 1
        elif string[i] == '5' and string[i+1] == '6':
            i += 2
        else:
            temp += string[i]
            i += 1
    return temp


if __name__ == '__main__':
    print(remove756(input()))