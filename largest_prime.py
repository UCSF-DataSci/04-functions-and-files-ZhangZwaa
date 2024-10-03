#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

    - Use command-line arguments to specify the upper limit 
    - Implement a function to check if a number is prime
    - Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

# You're on your own for this one. Good luck!
import argparse

def some_function(limit):
    # Generate Fibonacci number
    fibonacci_list = [0, 1]
    while (fibonacci_list[-1] + fibonacci_list[-2]) <= limit:
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    # Find out largest prime number in the list
    if max(fibonacci_list) < 2: # No prime number less than 2
         return None
    something = 2 # minimun of prime number
    for num in fibonacci_list:
        if num % 2 ==0 or num <= 2:
            continue
        statue = 0
        for n in range(3, int(num**0.5) + 1, 2):
            if num % n ==0:
                statue = 1
                break
        if statue == 1:
             continue
        else:
             if something < num:
                something = num
    return something

if __name__ == "__main__":
    # Do stuff here
    parser = argparse.ArgumentParser()
    parser.add_argument("limit", type=float, help="upper limit of number")

    args = parser.parse_args()
    fibonacci = some_function(args.limit)
    print(fibonacci)