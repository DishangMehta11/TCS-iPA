def isCorrect(number : str) -> bool:
	for i in range(len(number)-1):
		if abs(int(number[i]) - int(number[i+1])) != 1:
			return False
	return True


if __name__ == '__main__':
	print(isCorrect(input()))