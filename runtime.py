# write a program that will find the prime numbers from 1 to 100000 and measure the time it takes to find them.
import time
import sys

def prime(n):
    k = 0
    for i in range(2, n):
        for j in range(2, i):
            if(i % j == 0):
                break
            if(j == i-1):
                k = k + 1


start = time.time()
prime(int(sys.argv[1]))
end = time.time()
print((end - start) * 1000)