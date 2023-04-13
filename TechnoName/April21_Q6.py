def frequencyDigit(string: str) -> str:
    dic = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    for ch in string:
        if ch in dic:
            dic[ch] += 1
    return '{} {} {} {} {} {} {} {} {} {}'.format(dic['0'], dic['1'], dic['2'], dic['3'], dic['4'], dic['5'], dic['6'], dic['7'], dic['8'], dic['9'])

if __name__ == '__main__':
    print(frequencyDigit(input()))
