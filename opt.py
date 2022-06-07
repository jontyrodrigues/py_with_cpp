import sys
import time
n = int(sys.argv[1])

# better solution copied from https://stackoverflow.com/questions/55199558/program-to-find-all-the-prime-numbers-up-to-1-million-in-1-sec-or-as-close-to-it
def prime():
    is_prime = [False, False] + [True] * (n - 1)
    primes = [2]

    for j in range(4, n + 1, 2):
        is_prime[j] = False

    for i in range(3, n + 1, 2):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

start = time.time()
prime()
end = time.time()
print((end - start) * 1000)