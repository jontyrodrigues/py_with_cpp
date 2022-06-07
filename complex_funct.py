# this python scripts is used to automate the process of data gathering of a time complexity analysis.
# The data is stored in a csv file.
# The script will run the program for a number of times and store the data in a csv file.
# The program calculates the prime number from 1 to the number specified as the args.
# The program will return the time it takes to find the prime numbers.
# This data is stored in a csv file.

import subprocess

# Run a program with args and get the sdio data
def run_program():
    for i in range (1, 21):
        output = subprocess.getoutput("runtime.exe" + " " + str(i*10000))
        # put the output in a list and into a csv file
        output_list = [str(i*10000), output]
        with open('cpp.csv', 'a') as csvfile:
            csvfile.write(output_list[0] + "," + output_list[1] + "\n")
        output = subprocess.getoutput("python runtime.py" + " " + str(i*10000))
        # put the output in a list and into a csv file
        output_list = [str(i*10000), output]
        with open('py.csv', 'a') as csvfile:
            csvfile.write(output_list[0] + "," + output_list[1] + "\n")

run_program()
