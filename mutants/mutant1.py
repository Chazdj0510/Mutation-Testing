class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients  # Coefficients in descending order of degree

    def __add__(self, other):
        # Change the + to - (subtraction instead of addition)
        result = [self.coefficients[i] - other.coefficients[i] for i in range(len(self.coefficients))]
        return Polynomial(result)

    def __sub__(self, other):
        result = [self.coefficients[i] - other.coefficients[i] for i in range(len(self.coefficients))]
        return Polynomial(result)

    def __mul__(self, other):
        result = [self.coefficients[i] * other.coefficients[i] for i in range(len(self.coefficients))]
        return Polynomial(result)

    def evaluate(self, x):
        return sum(coef * (x ** i) for i, coef in enumerate(reversed(self.coefficients)))
