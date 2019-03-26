biggest = 0
for x in range(100,1000):
	for y in range(100,1000):
		a = x*y
		a = str(a)
		b = a[::-1]
		if a == b and biggest < int(a):
			biggest = int(a)
print("Solution is: "+str(biggest))