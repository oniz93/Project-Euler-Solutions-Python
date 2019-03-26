a = 0
b = 0
range_numbers = range(1,101)
for x in range_numbers:
    a = a + x
    b = b + x**2

solution = a**2 - b
print("Solution is: "+str(solution))