
input = open("input.txt", "r")

Lines = input.readlines()

sum = 0

matrix = []
counter = 0
for line in Lines:
	lineArray = []
	for char in line:
		lineArray.append(char)

	matrix.append(lineArray)
	counter += 1

for arrayIndex, array in enumerate(matrix):
	lastDigitIndex = -1
	for charIndex, character in enumerate(array):
		if(lastDigitIndex >= charIndex):
			continue
		if(character.isdigit()):
			firstDigitIndex = charIndex
			lastDigitIndex = charIndex
			while(lastDigitIndex < len(array) and array[lastDigitIndex].isdigit()):
				lastDigitIndex+= 1
			firstColumnCheckIndex = charIndex if charIndex == 0 else charIndex - 1
			lastColumnCheckIndex = charIndex if lastDigitIndex == len(array) - 1 else lastDigitIndex
			firstRowCheckIndex = arrayIndex if arrayIndex == 0 else arrayIndex - 1
			lastRowCheckIndex = arrayIndex if arrayIndex == len(matrix) - 1 else arrayIndex + 1

			include = False
			rowCheckerIndex = firstRowCheckIndex
			columnCheckerIndex = firstColumnCheckIndex

			numIndex = firstDigitIndex
			numString = ''
			while(numIndex <= lastDigitIndex):
				if(array[numIndex].isdigit()):
					numString = numString + array[numIndex]
				numIndex += 1
			print("Found: " + numString + " at " + str(arrayIndex) + " from " + str(firstDigitIndex) + " to " + str(lastDigitIndex))
			#print("firstRowCheckIndex: " + str(firstRowCheckIndex))
			#print("lastRowCheckIndex: " + str(lastRowCheckIndex))
			#print("firstColumnCheckIndex: " + str(firstColumnCheckIndex))
			#print("lastColumnCheckIndex: " + str(lastColumnCheckIndex))


			while(rowCheckerIndex <= lastRowCheckIndex):
				while(include == False and columnCheckerIndex <= lastColumnCheckIndex):
					print("Checking " + str(rowCheckerIndex) + ":" + str(columnCheckerIndex))
					checkValue = matrix[rowCheckerIndex][columnCheckerIndex]
					if(checkValue != '.' and not checkValue.isdigit() and not checkValue.isspace()):
						include = True
						print("Found symbol " + checkValue)
					columnCheckerIndex += 1
				rowCheckerIndex += 1
				columnCheckerIndex = firstColumnCheckIndex


			if(include):
				print(numString)
				sum += int(numString)

print(sum)