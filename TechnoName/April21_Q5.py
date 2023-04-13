def maxProfit(lst: list) -> int:
    high = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] < lst[j]:
                high = max(high, abs(lst[i] - lst[j]))
    return high


if __name__ == '__main__':
    print(maxProfit([int(input()) for _ in range(int(input()))]))
