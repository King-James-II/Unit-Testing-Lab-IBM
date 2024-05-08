# Math Module with Unit Testing

This repository contains a Python math module with unit tests for each function.

## Functions

1. `square(number)`: This function returns the square of a given number.

2. `double(number)`: This function returns twice the value of a given number.

3. `add(a, b)`: This function returns the sum of the given numbers. If both inputs are strings, they are concatenated.

## Unit Tests

The unit tests for each function are performed using the `unittest` module. Here's a brief explanation of the tests:

### `TestSquare`

- `test1`: Tests whether the `square` function correctly squares an integer (2), expecting the output to be 4.
- `test2`: Tests whether the `square` function correctly squares a float (3.0), expecting the output to be 9.0.
- `test3`: Tests whether the `square` function does not return the negative square of a negative number (-3), expecting the output to not be -9.

### `TestDouble`

- `test1`: Tests whether the `double` function correctly doubles an integer (2), expecting the output to be 4.
- `test2`: Tests whether the `double` function correctly doubles a negative float (-3.1), expecting the output to be -6.2.
- `test3`: Tests whether the `double` function correctly doubles zero (0), expecting the output to be 0.

### `TestAdd`

- `test1`: Tests whether the `add` function correctly adds two integers (2 and 4), expecting the output to be 6.
- `test2`: Tests whether the `add` function correctly adds two zeros (0 and 0), expecting the output to be 0.
- `test3`: Tests whether the `add` function correctly adds two floats (2.3 and 3.6), expecting the output to be 5.9.
- `test4`: Tests whether the `add` function correctly concatenates two strings ("hello" and "world"), expecting the output to be "helloworld".
- `test5`: Tests whether the `add` function correctly adds two float numbers (2.3000 and 4.300), expecting the output to be 6.6.
- `test6`: Tests whether the `add` function does not return zero when adding two negative numbers (-2 and -2), expecting the output to not be 0.
