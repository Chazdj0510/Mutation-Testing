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
   git clone https://github.com/Chazdj0510/Mutation-Testing.git
   cd Mutation-Testing
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
```

---

## Testing
The repository includes a test suite (`test_polynomial.py`) to ensure the functionality of the `Polynomial` class. Run the tests using:
```bash
pytest test_poly.py
```

Sample output:
```diff
==================== test session starts ====================
...
collected 8 items
test_poly.py .......                                  [100%]

==================== 8 passed in 0.12s ====================
```

---

## File Structure
- `polynomial.py`: Implementation of the `Polynomial` class.
- `test_poly.py`: Test cases using `pytest`.

---

## Acknowledgments
This project was developed as a hands-on example for polynomial operations and testing in Python.
