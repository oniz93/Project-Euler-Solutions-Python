counter = 20
while True:
	counter = counter + 20
	control = True
	for i in range(2,21):
		if counter%i != 0:
			control = False
			break
	if control == True:
		break
print("Solution is: "+str(counter))