def sieve(n):
    # Create a boolean array "prime[0..n]" and initialize 
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n + 1)]
    j=2
    while (j * j <= n): # only iterate to sqrt(n)
       # If prime[j] is not changed, then it is a prime 
       if (prime[j] == True): # Update all multiples of p
          yield(j)
          for i in range(j ** 2, n + 1, j): 
             prime[i] = False
       j += 1
    # Print all prime numbers
    for p in range(j, n + 1):
       if prime[p]:
          yield (p)
    return

