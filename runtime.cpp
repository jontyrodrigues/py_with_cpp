// write a program that will find the prime numbers from 1 to 10000 and measure the time it takes to find them.
#include <iostream>
#include <chrono>
using namespace std;

void prime(int n)
{
    int i, j;
    for (i = 2; i <= n; i++)
    {
        for (j = 2; j <= i; j++)
        {
            if (i % j == 0)
                break;
        }
    }
}

int main(int argc, char** argv)
{
   int n = atoi(argv[1]);
   std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
   prime(n);
   std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
   std::cout << std::chrono::duration_cast<std::chrono::milliseconds>(end - begin).count();
}


