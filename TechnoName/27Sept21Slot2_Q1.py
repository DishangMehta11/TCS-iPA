import time

def coins(number: int, cache: dict = {}) -> int:
    if number == 1 or number == 0:
        return 1
        
    elif number == 2:
        return 2

    if number in cache:
        return cache[number]

    cache[number] = coins(number-1, cache) + coins(number-3, cache)
    return cache[number]

if __name__ == '__main__':
    start = time.perf_counter()
    print(coins(int(input())))
    end = time.perf_counter()
    # print(end-start)