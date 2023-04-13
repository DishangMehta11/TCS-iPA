def countStudents(lst: list[int]) -> int:
    count = 0
    for i in range(1, len(lst)-1):
        if lst[i-1] > lst[i] and lst[i] < lst[i+1]:
            count += 1
    return count


if __name__ == '__main__':
    print(countStudents([int(input()) for _ in range(int(input()))]))