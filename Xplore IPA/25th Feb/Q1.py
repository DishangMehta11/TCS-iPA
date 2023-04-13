def search(lst, search):
    count = 0
    for ele in lst:
        if search in ele:
            count += 1
    return count


print(search([input() for _ in range(int(input()))], input()))
