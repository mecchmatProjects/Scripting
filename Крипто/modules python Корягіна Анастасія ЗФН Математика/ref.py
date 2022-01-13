# module fractional
from fractions import Fraction
from decimal import Decimal
a=Fraction(Decimal('1.5'))
# 1.5-> 3/2
b=Fraction(Decimal('3'))
# 3-> 3/1
print(a,b)
Fraction()
# Fraction(0, 1)
print(Fraction(numerator=5, denominator=9))
print(Fraction(2, 3))
a=Fraction(3,7)
b=Fraction(7,19)
print("a+b:",a+b,"\n a-b:",a-b,"\n a*b:",a*b,"\n a/b+3:",a/b+3,"\n a**b:",a**b)


