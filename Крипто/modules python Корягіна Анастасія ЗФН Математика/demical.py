from decimal import Decimal
x=Decimal("0.2")
print(x+x+x)
number = Decimal("0.2356")
number = number.quantize(Decimal("1.00"))
print(number)
number = Decimal("0.555678")
print(number.quantize(Decimal("1.0000")))

number = Decimal("0.999")
print(number.quantize(Decimal("1.0")))