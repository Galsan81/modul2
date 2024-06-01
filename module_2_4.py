numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 75, 33]
not_primes = []
primes = []
n = 0
i = 0

for i in numbers:
    m = i

    if m!=1:
        is_prime = True
        for j in range(2, m):

            if m % j == 0 :
                is_prime=False
                #is_prime = True
        if is_prime==True :
            primes.append(m)
        else:
            not_primes.append(m)
            # else:
        # break
    # for k in range(2, i):
    #  if i % k ==
print('Primes:', primes)
print('Not primes:', not_primes)
