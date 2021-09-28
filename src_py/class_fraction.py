class Fraction(object):
    '''Defines a Fraction type that has an integer numerator and a non-zero integer denominator'''

    def __init__(self, num=0, denom=1):
        ''' Creates a new Fraction with numberator num and denominator denom'''
        self.numerator = num
        if denom != 0:
            self.denominator = denom
        else:
            raise ZeroDivisionError
            
    def __add__(self, other):
        numerator1 = self.numerator * other.denominator
        numerator2 = other.numerator * self.denominator
        return Fraction(numerator1 + numerator2, self.denominator * other.denominator)
    
    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
    
    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator
    
    def __repr__(self):
        return 'Fraction({}, {})'.format(self.numerator, self.denominator)    
    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)     

    
class ReducedFraction(Fraction):
    """A subclass of Fraction"""
    def __init__(self, numerator, denominator=1):
        Fraction.__init__(self, numerator, denominator)
        self.__reduce__()

    def __reduce__(self):
        gcd = findgcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator / gcd)
        self.denominator = int(self.denominator / gcd)
        
    def __mul__(self, other):
        unreduced_fraction = Fraction.__mul__(self, other)
        return ReducedFraction(unreduced_fraction.numerator, unreduced_fraction.denominator)
        
        
    def __add__(self, other):
        unreduced_fraction = Fraction.__add__(self, other)
        return ReducedFraction(unreduced_fraction.numerator, unreduced_fraction.denominator)
    

    def __repr__(self):
        return 'ReducedFraction({}, {})'.format(self.numerator, self.denominator)
        
        
def findgcd(x, y):
    '''Returns the Greatest Common Divisor of x and y. Assumes x and y are positive integers.'''
    smaller = min(x, y)
    for i in range(int(smaller), 1, -1):
        if x % i == 0 and y % i == 0:
            return i
    return 1    


class MixedNumber(ReducedFraction, Fraction):
    def __init__(self, whole_part, fraction_part):
        self.whole_part = whole_part
        ReducedFraction.__init__(self, fraction_part.numerator, fraction_part.denominator)
        
    def __add__(self, other):
        reduced_fraction = ReducedFraction.__add__(self, other)
        plus = 0
        if reduced_fraction.numerator >= reduced_fraction.denominator:
            while reduced_fraction.numerator >= reduced_fraction.denominator:
                reduced_fraction.numerator -= reduced_fraction.denominator
                plus += 1
        return MixedNumber(self.whole_part + other.whole_part + plus, reduced_fraction)
        
    def __repr__(self):
        return 'MixedNumber({}, ReducedFraction({}, {}))'.format(self.whole_part, self.numerator, self.denominator)
        
    def __str__(self):
        return '{} and {}/{}'.format(self.whole_part, self.numerator, self.denominator)
    
    
    
x = MixedNumber(3, Fraction(1, 3))
y = MixedNumber(-1, Fraction(2, 5))
z = x + y
print(z)
print(repr(z))