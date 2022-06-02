# write a program that will find the prime numbers from 1 to 100000 and measure the time it takes to find them.
import time

def prime(n):
    for i in range(2, n):
        for j in range(2, i):
            if(i % j == 0):
                break

start = time.time()
prime(200000)
end = time.time()
print((end - start) * 1000)