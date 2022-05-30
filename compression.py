import re



def bits2Num (input,bits): 		# input a number, and how many bits, and it will spit out it's number counterpart
	
	input_str = str(input) 		# convert to a str

	# add commas to the string
	input_comma = (",".join(input_str[i:i+bits] for i in range(0, len(input_str), bits)))

	# split the string into a list at east comma (bit_size)
	input_list = input_comma.split (",")


	# now convert the list into numbers

	# initalize the variable to store all the numbers concatenated
	finishedValue = ""

	# here we use the binaryToCount() function to change our binary, to a specific value, then concatenate them together
	for x in input_list:
		finishedValue = finishedValue + str(binaryToCount(x))

	return (finishedValue)

	#print (input_list)

	#return input;
#######################


""""""
# this takes a single binary of x length bits (assumes the size is the count of bits) and turns it into a count of what number it represents
def binaryToCount(binary_number):


	#current_number = str(binary_number)
	current_number = int(binary_number)

	# the spot we add the binary values to
	binary_count = 0

	#how much the current binary value is worth
	current_value = 1

	# initialize the loop length based on the length of the input variable
	loopCount = len(str(current_number))
	i = 0 		# start the index at 0
	while (i <= loopCount):

		# compare the last digit (with [-1]) but it needs to be a str to use substring, but we want to compare as int
		if (int(str(current_number)[-1]) == 1):

			# if it is a 1, add to binary_count, the amount the current bit is worth (based on (current_value))
			binary_count = binary_count + current_value

		# this takes off the very last digit
		current_number = current_number // 10

		# this doubles the current_value of the bit we are observing next (in binary, it doubles each time)
		current_value = current_value * 2

		# now increase the index by 1
		i = i + 1

	# return the binary_count (which is where we've been adding all the bit values to)
	return binary_count



# call the function inside a print (to get an output for a specific binary number)
#print(binaryToCount("11100011"))

# this should be called as a string, to avoid any binary number that starts with a leading 0, erroring out.

""""""


# this function takes a starting binary number and adds a needed number of zeroes
def addZeroes(startNum, zeroesNeeded):
	finalNum = startNum

	i = 0
	while (i < zeroesNeeded):
		finalNum = str(finalNum) + "0"
		i = i + 1
	
	return int(finalNum)


#this takes a number, and adds a space every x bits for readability
def binaryPrint(number, bits):

	number_str = str(number)

	return " ".join(number_str[i:i+bits] for i in range(0, len(number_str), bits))


############################
# take any int and turn it into a binary bit chunk (of any desired bit length) !Must be greater than 5 bits, for digits up to 9!

# all numbers will be 5 bit, but with 0's at the start as needed
def numberToBinary(input, binarySize):

	# verify that it's a str, or it will cut off leading 0's
	input = str(input)

	# initialize the variable
	leadingZeroes = ""

	# loop and add a specific number of zeroes to the varaible
	loopSize = binarySize - 5
	i = 1
	while (i <= loopSize):
		leadingZeroes = leadingZeroes + "0"
		i = i + 1

	# use regex sub to swap each number with it's binary counterpart (with a leading number of zeroes based on binarySize)
	input = re.sub('0', leadingZeroes + '00000',input)
	input = re.sub('1', leadingZeroes + '00001',input)
	input = re.sub('2', leadingZeroes + '00010',input)
	input = re.sub('3', leadingZeroes + '00011',input)
	input = re.sub('4', leadingZeroes + '00100',input)
	input = re.sub('5', leadingZeroes + '00101',input)
	input = re.sub('6', leadingZeroes + '00110',input)
	input = re.sub('7', leadingZeroes + '00111',input)
	input = re.sub('8', leadingZeroes + '01000',input)
	input = re.sub('9', leadingZeroes + '01001',input)

	return input



#print(binaryPrint(numberToBinary("123456789", 6),6))


print(binaryToCount(numberToBinary("123456789",5)))




bit_size = 8

#startingNum = 1000100100001010011100
startingNum = "000000010000001000000011000001000000010100000110000001110000100000001001"

#5 is the number we need to get to, then we get the remainder once we divide by 5, and check for the difference (1)
zeroesAdded = bit_size-(len(str(startingNum))%bit_size)

# here we add x number of zeros to get up to  5 bit number
numAdjusted = addZeroes(startingNum,zeroesAdded)


#print(binaryPrint(numAdjusted,bit_size))




#print(bits2Num(numAdjusted,bit_size))


#print(binaryPrint("000001000010000011000100000101000110000111001000001001", 6))



