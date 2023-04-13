def maxInterviews(starttime, endtime) -> int:
    count = 1
    end = endtime[0]
    for i in range(len(starttime) - 1):
        if end <= starttime[i+1]:
            count += 1
            end = endtime[i+1]

    return count

if __name__ == "__main__":
    n = int(input())
    starttime = [int(input()) for _ in range(n)]
    endtime = [int(input()) for _ in range(n)]

    print(maxInterviews(starttime, endtime))