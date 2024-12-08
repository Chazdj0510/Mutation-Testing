# Polynomial Operations - Mutation Testing
## Project Overview
This project implements basic polynomial operations such as addition, subtraction, multiplication, and evaluation for polynomials represented by their coefficients. The operations are implemented within the `Polynomial.py` class.

## Mutation Testing Overview
Mutation testing is a technique used to evaluate the effectiveness of tests by intentionally introducing small modifications (mutants) into the code. If the test suite fails to detect a mutant, it indicates that the test suite is not comprehensive enough to catch certain types of errors.

In this project, I created several mutants of the original `Polynomial.py` class to test the robustness of the test suite.

## Mutants Introduced
The following mutants were introduced into the code, each representing a small change to the logic of the `Polynomial.py` class:

1. Mutant 1: Addition Mutation

   - Changed the `+` operator in the `__add__` method to `-`, reversing the addition to subtraction.
   - This tests if the code handles the change from adding to subtracting polynomial coefficients.
2. Mutant 2: Multiplication Mutation

   - Changed the `*` operator in the `__mul__` method to `+`, turning polynomial multiplication into polynomial addition.
   - This tests if the code distinguishes between multiplication and addition.
3. Mutant 3: Evaluation Mutation

   - Modified the `evaluate` method to ignore the first coefficient during polynomial evaluation.
   - This tests whether the evaluation method correctly handles the entire polynomial.
4. Mutant 4: Logical Mutation

   - Changed the equality check `==` in the `__add__` method to `!=`, altering the logic of the polynomial addition.
   - This tests whether the code catches logical errors in the polynomial addition logic.

## Mutation Testing Process
1. Each mutant file was placed in the mutants/ folder along with a test file placed in the tests/ folder.
2. The pytest testing framework was used to run the tests for each mutant.
3. The results were evaluated based on whether the tests detected the mutant or not:
   - If the test fails with the mutant, the mutant is considered killed (i.e., the test suite is effective).
   - If the test passes with the mutant, the mutant survives (i.e., the test suite is ineffective against that type of change).

## Test Results

| Mutant                               |   Status   | Test Result |  Notes                                               |
| :----------------------------------- | :--------: | :---------: | :--------------------------------------------------- |
| Mutant 1 (Addition Mutation)         |  Killed    |    Fails    | The test suite detected the addition mutation.       | 
| Mutant 2 (Multiplication Mutation)   |  Killed    |    Fails    | The test suite detected the multiplication mutation. |
| Mutant 3 (Evaluation Mutation)       |  Killed    |    Fails    | The test suite detected the evaluation mutation.     |
| Mutant 4 (Logical Mutation)          |  Survived  |    Pass     | The test suite did not detect the logical mutation.  |

## Conclusion
Mutants Killed: 3 out of 4 mutants were successfully killed by the test suite, indicating that the tests are effective at catching certain types of errors.
Mutants Survived: 1 mutant survived, which suggests that the test suite could be improved by adding tests for logical correctness in polynomial operations.

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
The repository includes a test suite (`test_poly.py`) to ensure the functionality of the `Polynomial` class. Run the tests using:
```bash
pytest test_poly.py
```

Output:
```diff
==================== test session starts ====================
...
collected 8 items
test_poly.py .......                                  [100%]

==================== 8 passed in 0.12s ====================
```

### Mutant Files (After Mutations)
#### Mutant 1 - Addition Mutation (`mutant1.py`)
This mutant changes the addition operator (`+`) to a subtraction operator (`-`).


---

## File Structure
- `polynomial.py`: Implementation of the `Polynomial` class.
- `test_poly.py`: Test cases using `pytest`.

---

## Acknowledgments
This project was developed as a hands-on example for polynomial operations and testing in Python.
