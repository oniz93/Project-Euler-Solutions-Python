
start_num = 1
logest_chain = 0
big_num_long_chain = 0
while start_num < 1000000:
	# I start from 2
	start_num = start_num + 1

	# The chain length starts from 1, the starting number is counted in the chain
	chain_length = 1
	chain_number = start_num

	# Repeat the process until the number isn't 1
	while chain_number != 1:

		# Check if the number is even
		if chain_number%2 == 0:
			chain_number = chain_number / 2
			chain_length = chain_length + 1
		# Otherwise is odd
		else:
			chain_number = (3 * chain_number) + 1
			chain_length = chain_length + 1
	if logest_chain < chain_length:
		logest_chain = chain_length
		big_num_long_chain = start_num
	#print("Start num: "+str(start_num)+" | Length: "+str(chain_length))

print("Solution is: "+str(big_num_long_chain))