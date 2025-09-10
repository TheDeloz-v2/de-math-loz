# de-math-loz

A Python package containing basic mathematical functions.

## Functions

- square(n): Returns the square of a number
- factorial(n): Returns the factorial of a number
- is_prime(n): Checks if a number is prime
- gcd(a, b): Returns the greatest common divisor
- lcm(a, b): Returns the least common multiple

## Installation

`hash
pip install -e .
`

## Usage

`python
from src.math_functions import square, factorial

print(square(5))  # 25
print(factorial(5))  # 120
`

## Testing

`hash
pytest tests/
`