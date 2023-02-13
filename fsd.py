
from math import log10, exp, pi, sqrt, fabs

###
# function to calculate probability density function
# Args:
# x - float, number to calculate digits
# mu - mean (from normal distibution)
# sigma - standart deviation (from normal distibution)
# Return:
# float, value of distibution
def PDFFunction (x,mu = 5,sigma = 1):
    power = -(1/2)*((x-mu)/sigma)**2
    #print("bruh ", x)
   # print("lol ", exp(power))
    y = (1/sqrt(2*pi)) * exp(power)
    return y

###
# function to calculate definite integral
# using Simpson`s rule
# Args:
# func - function
# a - float, lower bound of integral
# b - float, upper bound of integral
# h - float, precision
def Integral (func, a, b, h=0.0001):
    
    n = (b - a) / h

    s = func(a) + func(b)
    for i in range(2, int(n) - 1, 2):
        s += 2 * func(a + i * h)
    for i in range(1, int(n), 2):
        s += 4 * func(a + i * h)
    return s * h / 3

###
# function to calculate FSD score
# Args:
# N - int, number to calculate digits
# PDFFunction - function, probability density function, R->R
# eps - float, precision
# Return:
#  float, fsd score
def fsdScore(N, PDFFunction,eps=0.0001):
    s = 0
    for d in range (1, 10):
        ProbBenford = log10(d + 1) - log10(d)
        ProbPDF = Integral(PDFFunction,log10(d),log10(d + 1))
        #for n in range(1, N ): ## Fignya!
        n = 1
        inner = eps + 1

        while fabs(inner)>eps:
            innerPositive = Integral(PDFFunction,n + log10(d),n + log10(d + 1))
            innerNegative = Integral(PDFFunction,-n + log10(d),-n + log10(d + 1))

            inner = innerPositive + innerNegative 
            ProbPDF += inner
            n += 1
        s += fabs(ProbPDF - ProbBenford)
    return s/9
#print (fsdScore(123, PDFFunction))

#print(PDFFunction(5))
#print (Integral(PDFFunction0, 0 + log10(1), 0 + log10(2)))
