import numpy
primes = [2,3,5,7]
possiblePrime = 9
while possiblePrime < 2000000:
    
    possiblePrime = possiblePrime + 2
    # Assume number is prime until shown it is not. 
    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1):
        if possiblePrime % num == 0:
            isPrime = False
            break
      
    if isPrime:
        primes.append(possiblePrime)

print("Solution is: "+str(numpy.sum(primes)))