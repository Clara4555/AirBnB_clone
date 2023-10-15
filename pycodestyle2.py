#!/usr/bin/python3
# A simple Python script to calculate the area of a rectangle.

def calculate_rectangle_area(length, width):
    return length * width


if __name__ == "__main__":
    length = 5
    width = 3
    area = calculate_rectangle_area(length, width)
    print(f"The area of the rectangle is: {area} square units")
