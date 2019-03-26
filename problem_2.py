import numpy
a = 1
b = 1
even_elements = []
while b <= 4000000:
	c = a+b
	if c%2 == 0:
		even_elements.append(c)
	a = b
	b = c
print("The result is: "+str(numpy.sum(even_elements)))