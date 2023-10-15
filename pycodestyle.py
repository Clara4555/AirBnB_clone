#!/usr/bin/python3
# This is a Python script calculates the sum of even numbers from 1 to 10.

def sum_of_evens():
    total = 0

    for num in range(1, 11):
        if num % 2 == 0:
            total += num
    return total


if __name__ == "__main__":
    result = sum_of_evens()
    print("The sum of even numbers from 1 to 8 is:", result)
