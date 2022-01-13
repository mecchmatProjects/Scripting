#20.3_з
import matplotlib.pyplot as plt;
import numpy as np;

def taylor(x, n):
    y = 0;
    t2 = x;
    t1 = x;
    for i in range(1, n):
        y = y + t2;
        denom = (2*i + 1);
        t1 = t1*x*x;
        t2 = t1 / denom;
    return 2*y;

a = float(input ("Введіть a: "));
b = float(input ("Введіть b: "));
m = int(input ("Введіть m: "));

x = np.linspace(a , b, 501); # Интервал между a и b заполнен 501 точкой
real = np.log((1 + x)/(1 - x)); # массив значений cамой функции
taylor_m = taylor(x, m);
plt.plot(x, real, 'r-',
         x, taylor_m, 'k--',
         linewidth=3.0);
plt.title('ln(1+x)/(1-x) and It\'s Taylor Expansion') # Заголовок графика
plt.legend(['ln(1+x)/(1-x)', 'Taylor Expansion'])
plt.xlim(a,b) # Интервал графика по иксу
plt.ylim(-5,5) # Интервал графика по игреку
plt.show() # показ графика





