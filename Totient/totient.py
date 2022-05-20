import math

from sieve import sieve

#The function phi accepts a prime factorization list and returns the Euler totient function for that factorization (e.g., 8 for the factorization listed above).
def phi(list):
    prime_list, return_value = list, 1
    for n in prime_list:
        #This could be done in one line, but I think it's too complicated to read and uncessary because the code is only a few lines to begin with. 
        i = math.pow(n[0], n[1]) - math.pow(n[0], n[1] - 1) 
        return_value *= i
    return(return_value)

#The function prime_fac accepts an integer parameter n and returns the prime factorization of n as a list of factors and their powers.  
#For example, the prime factorization of 24 is 2331 so prime_fac(24) would return the list [(2,3),(3,1)].  The factors are in ascending order.  
#This function must use the sieve code provided as its generator of prime numbers.    
def prime_fac(number):
    n, list, counter = number, [], 0
    #cannot do this more pythonically because n needs to be instantiated before it can be passed to sieve
    factors = sieve(n) 
    for potential in factors:
        if (n % potential) == 0:
            counter = 0
            while n % potential == 0:
                n //= potential
                counter += 1
            list.append((potential, counter))
            #this could be done in one line, but I'd prefer not to sort while returning
    returnList = sorted(list) 
    #just in case it isn't sorted
    return(returnList) 