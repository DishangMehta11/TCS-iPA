def countHSL(string: str) -> int:
    s = ''
    count = 0
    for i in range(len(string)):
        if string[i] == 'H' and 'S' in string[i+1:] and 'L' in string[i+2:]:
            count += 1
    return count


if __name__ == '__main__':
    print(countHSL(input()))