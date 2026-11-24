# C Statistics Program with Python Automated Testing

Introduction:
I created a C program to calculate basic statistics from a list of numbers. Then, I created a Python script to automatically test the C program. The main purpose of this project is to learn how Python can be used for basic automation 

The Python script:
Compiles the C program using GCC.
Runs the C program with different input values.
Captures the program output.
Compares the actual results with the expected results.
Displays PASS or FAIL for each test.
Generates a test report in a text file.

The C program performs the following operations:
Finds the minimum value.
Finds the maximum value.
Calculates the mean.
Calculates the median.
Sorts the input values in descending order.
Input Validation
Accepts a minimum of 1 and a maximum of 40 numbers.
Accepts numbers between 0 and 255.
Rejects invalid inputs such as negative numbers.

Testing:
Test Case 1 - Normal input
Input - 10, 20, 30
Purpose - Check basic calculations

Test Case 2 - same input value
Input - 25
Purpose - Check a single-number input

Test Case 3 - Boundary values
Input - 0, 255
Purpose - Check minimum and maximum allowed values

Test Case 4 - Negative input
Input - -5, 10
Purpose - Check invalid input handling

Command to execute the script:
    python test_stats.py

Test results:
Stored in test_report.txt 

## Author
Nandhini Rajapandiyan
