import numpy
import math
import pprint
pp = pprint.PrettyPrinter(indent=4)


from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))



dictnumbers = dict()
for x in range(1,10001):
	tot = numpy.sum(list(factors(x))[:-1])
	if tot in dictnumbers:
		dictnumbers[tot].append(x)
	else:
		dictnumbers[tot] = [x]

solution = 0
for k,v in dictnumbers.items():
	for vv in v:
		if vv in dictnumbers.keys() and k in dictnumbers[vv] and vv < 10000 and k < 10000 and vv != k:
			print(str(vv)+" - "+str(k))
			solution = solution + vv + k
solution = solution / 2
pp.pprint(dictnumbers[5209])
pp.pprint(factors(5))
print("Solution is: "+str(solution))