import sys

input = open("input.txt", "r")

Lines = input.readlines()

sum = 0

for line in Lines:
	colonPosition = line.find(':')
	gameNumber = line[5:colonPosition].strip()

	games = line[colonPosition+1:len(line)].split(';')
	maxRed = 0
	maxGreen = 0
	maxBlue = 0

	#print(gameNumber)
	gameCounter = 1
	legal = True
	for game in games:
		#print(gameCounter)
		gameCounter+= 1
		gameResults = game.split()
		#print(gameResults)
		trailingNumber = 0
		for element in gameResults:
			strippedElement = element.strip(',')
			if(strippedElement.isnumeric()):
				trailingNumber = int(strippedElement)
			else:
				if(strippedElement == "red" and trailingNumber > maxRed):
					maxRed = trailingNumber
				if(strippedElement == "blue" and trailingNumber > maxBlue):
					maxBlue = trailingNumber
				if(strippedElement == "green" and trailingNumber > maxGreen):
					maxGreen = trailingNumber
			

	print("Red: " + str(maxRed))
	print("Blue: " + str(maxBlue))
	print("Green: " + str(maxGreen))

	print("Power: " + str(maxRed * maxBlue * maxGreen))

	sum += maxRed * maxBlue * maxGreen




print(sum)



	
