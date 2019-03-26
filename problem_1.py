import numpy
found = []
for i in range(3, 1000):
	if i%3 == 0 or i%5==0:
		found.append(i)

print("Result is: "+str(numpy.sum(found)))