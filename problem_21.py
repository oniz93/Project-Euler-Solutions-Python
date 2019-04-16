import numpy
import math
import pprint
pp = pprint.PrettyPrinter(indent=4)


from functools import reduce

def factors(n):    
    return sorted(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

amicables = list()
for x in range(1,10001):
	tot = numpy.sum(list(factors(x))[:-1])

	if tot > 1 and tot != x:
		tot2 = numpy.sum(list(factors(tot))[:-1])

		if tot2 == x:
			amicables.append([tot,x])

solution = 0
for v in amicables:
	solution = solution + v[0] + v[1]
solution = solution / 2
print("Solution is: "+str(solution))