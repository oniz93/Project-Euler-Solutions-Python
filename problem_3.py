number = 600851475143
new_number = number
largestFact = 0
 
counter = 2
while counter * counter <= new_number:
    if new_number % counter == 0:
        new_number = new_number / counter
        largestFact = counter;
    else:
        counter = counter + 1
if new_number > largestFact:
    largestFact = new_number;

print("Solution is: "+str(largestFact))