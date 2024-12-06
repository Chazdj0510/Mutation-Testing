# Mutation-Testing
# Polynomial Operations in Python

This project provides a `Polynomial` class in Python that supports creating, evaluating, and performing various operations on polynomials, such as addition, subtraction, multiplication, and finding roots using the bisection method. Additionally, this repository includes a comprehensive test suite using `pytest`.

---

## Features

- **Polynomial Representation**: Create polynomials using a list of coefficients.
- **String Representation**: View the polynomial in standard mathematical notation.
- **Arithmetic Operations**: Add, subtract, and multiply polynomials.
- **Evaluation**: Evaluate the polynomial at specific values of `x`.
- **Root Finding**: Locate roots of polynomials using the bisection method.

---

## Getting Started

### Prerequisites
- Python 3.6 or higher
- `pytest` library for testing

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/repo-name.git
   cd repo-name
2. Install `pytest`:
   ```bash
   pip install pytest

---

## Usage

### Creating and Using Polynomials
```python
from polynomial import Polynomial

# Create polynomials
poly1 = Polynomial([3, 0, 2])  # Represents 3x^2 + 2
poly2 = Polynomial([1, -1])   # Represents x - 1

# Perform operations
poly_sum = poly1 + poly2
poly_diff = poly1 - poly2
poly_product = poly1 * poly2

# Evaluate a polynomial at x = 2
value = poly1.evaluate(2)

# Find a root using the bisection method
root = poly1.find_root_bisection(0, 5)
```

### Running the Example Code
To run the example usage provided in `polynomials.py`, excute:
```bash
python polynomial.py
