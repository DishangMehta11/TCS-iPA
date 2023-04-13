def autoPilot(directions: str) -> bool:
    N = W = S = E = 0
    for ch in directions:
        if ch == 'N':
            N += 1
        elif ch == 'W':
            W += 1
        elif ch == 'S':
            S += 1
        else:
            E += 1

    return N == S and W == E


if __name__ == '__main__':
    print('Returned Successfully' if autoPilot(input()) else 'Not returned successfully')