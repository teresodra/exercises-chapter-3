from numbers import Number


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):

        if isinstance(other, Polynomial):
            coefs = []
            for i in range(self.degree() + other.degree() + 1):
                initial_use_deg = tuple([] for _ in range(i+1))
                self_use_deg = initial_use_deg + self.coefficients()[:i+1]
                other_use_deg = initial_use_deg + other.coefficients()[:i+1]
                new_coeff = 0
                for j in range(i+1):
                    new_coeff += self_use_deg[j] * other_use_deg[-j]
                coefs.append(new_coeff)

            return Polynomial(tuple(coefs))

        elif isinstance(other, Number):
            return Polynomial(tuple(elem * other for elem in self.coefficients))

        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        return self + (-1) * other

    def __rsub__(self, other):
        return (-1) * self + other

    def __pow__(self, other):

        if isinstance(other, int) and other >= 0:
            power = 1
            for _ in range(other):
                power *= self
            return power
        
        else: 
            return NotImplemented

    def __call__(self, scalar):
        return sum(scalar * coef ^ i for i, coef in enumerate(self.coefficients))