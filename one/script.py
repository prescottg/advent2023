input = open("input.txt", "r")

Lines = input.readlines()
 
sum = 0
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
    firstDigit = '0';
    lastDigit = '0';
    firstDigitPosition = 1000
    lastDigitPosition = -1
    pos = 0
    for char in line:
    	if(char.isdigit()):
    		if(firstDigit == '0'):
    			firstDigit = char
    			firstDigitPosition = pos
    		lastDigit = char
    		lastDigitPosition = pos
    	pos +=1

    print("Line{}: {}".format(count, firstDigit+lastDigit))

    numberStrings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    firstStringPosition = 1000
    lastStringPosition = -1
    firstString = ""
    lastString = ""
    for number in numberStrings:
    	firstPosition = line.find(number)
    	if(firstPosition >=0 and firstPosition < firstStringPosition):
    		firstString = number
    		firstStringPosition = firstPosition
    	lastPosition = line.rfind(number)
    	if(lastPosition > lastStringPosition):
    		lastString = number
    		lastStringPosition = lastPosition


    print("Line{}: {}".format(count, firstString+lastString))

    firstStringValue = 0;
    lastStringValue = 0;

    if(firstStringPosition != 1000):
    	match firstString:
    		case "one":
    			firstStringValue = "1"
    		case "two":
    			firstStringValue = '2'
    		case "three":
    			firstStringValue = '3'
    		case "four":
    			firstStringValue = '4'
    		case "five":
    			firstStringValue = '5'
    		case "six":
    			firstStringValue = '6'
    		case "seven":
    			firstStringValue = '7'
    		case "eight":
    			firstStringValue = '8'
    		case "nine":
    			firstStringValue = '9'

    if(lastStringPosition != -1):
    	match lastString:
    		case "one":
    			lastStringValue = '1'
    		case "two":
    			lastStringValue = '2'
    		case "three":
    			lastStringValue = '3'
    		case "four":
    			lastStringValue = '4'
    		case "five":
    			lastStringValue = '5'
    		case "six":
    			lastStringValue = '6'
    		case "seven":
    			lastStringValue = '7'
    		case "eight":
    			lastStringValue = '8'
    		case "nine":
    			lastStringValue = '9'

    first = 0
    last = 0

    print("{}: {}".format("First Digit Position", firstDigitPosition))
    print("{}: {}".format("First String Position", firstStringPosition))
    print("{}: {}".format("Last Digit Position", lastDigitPosition))
    print("{}: {}".format("Last String Position", lastStringPosition))

    if(firstStringPosition < firstDigitPosition):
    	first = firstStringValue
    else:
    	first = firstDigit

    if(lastStringPosition >lastDigitPosition):
    	last = lastStringValue
    else:
    	last = lastDigit


    print("Line{}: {}".format(count, first+last))

    sum += int(first+last)

print(sum)

