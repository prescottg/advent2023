input = open("input.txt", "r")

Lines = input.readlines()

sum = 0

scratchCardCounter = {}

counter = 1

while(counter <= 186):
	scratchCardCounter.setdefault(counter, 1)
	counter += 1

cardCounter = 1

for line in Lines:
	colonPosition = line.find(':')

	card = line[colonPosition+1:len(line)].split('|')
	winningNumbers = card[0].split()
	cardNumbers = card[1].split()
	#print(winningNumbers)
	#print(cardNumbers)

	scratchCardsWon = 0;
	for cardNumber in cardNumbers:
		if(cardNumber in winningNumbers):
			scratchCardsWon += 1
	#print(scratchCardsWon)
	wonCounter = 1;	

	while(wonCounter <= scratchCardsWon):
		temp = scratchCardCounter.get(cardCounter)
		wonCardNumber = cardCounter + wonCounter
		tempTwo = scratchCardCounter.get(wonCardNumber)
		scratchCardCounter.update({wonCardNumber: temp + tempTwo})
		wonCounter += 1
	cardCounter += 1

counter = 1

while(counter <= 186):
	sum += scratchCardCounter.get(counter)
	counter += 1


print(sum)
