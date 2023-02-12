from math import log10, exp, pi, sqrt, fabs


def PDFFunction (x,mu = 5,sigma = 1):
    power = -(1/2)*((x-mu)/sigma)**2
    #print("bruh ", x)
   # print("lol ", exp(power))
    y = (1/sqrt(2*pi)) * exp(power)
    return y

def PDFFunction0 (x):
    return 1/9

def Integral (func, a, b, h=0.0001):
    
    n = (b - a) / h

    s = func(a) + func(b)
    for i in range(2, int(n) - 1, 2):
        s += 2 * func(a + i * h)
    for i in range(1, int(n), 2):
        s += 4 * func(a + i * h)
    return s * h / 3


def fsdScore(N, PDFFunction,eps=0.0001):
    s = 0
    for d in range (1, 10):
        ProbBenford = log10(d + 1) - log10(d)
        ProbPDF = 0
        #for n in range(1, N ): ## Fignya!
        n = 0
        inner = eps + 1

        while fabs(inner)>eps:
            inner = Integral(PDFFunction,n + log10(d),n + log10(d + 1))
            ProbPDF += inner 
            n += 1
        s += fabs(ProbPDF - ProbBenford)
    return s/9
#print (fsdScore(123, PDFFunction))

#print(PDFFunction(5))
#print (Integral(PDFFunction0, 0 + log10(1), 0 + log10(2)))