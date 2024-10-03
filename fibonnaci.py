#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""
import argparse

def some_function(limit, save_path):
    # Generate
    fibonacci = [0, 1]
    while (fibonacci[-1] + fibonacci[-2]) <= limit:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    something = fibonacci
    # Save the Fibonacci sequence
    try:
        with open(save_path, 'w') as f:
            for num in fibonacci:
                f.write(f"{num}\n")

    except IOError:
        print("Something went wrong when trying to write the data!")
    
    return something


if __name__ == "__main__":
    # Do stuff here
	parser = argparse.ArgumentParser()
	parser.add_argument("limit", type=float, help="upper limit of number")
	parser.add_argument("path", type=str, help="write the path name")

	args = parser.parse_args()
	fibonacci = some_function(args.limit, args.path)