def extract(string: str) -> str:
    letter = ''
    special = ''
    for ch in string:
        if ch.isalpha():
            letter += ch
        elif ch.isdigit():
            continue
        else:
            special += ch
    return letter + special


if __name__ == "__main__":
    print(extract(input()))