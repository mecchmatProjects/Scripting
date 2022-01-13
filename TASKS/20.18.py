#20.18
import matplotlib.pyplot as plt
import numpy as np
import np.random as rnd

test_num = 10000

def prob(ntrials, money):
    vygrash = money
    for i in range (1,ntrials+1):
        vygrash = vygrash - 1

        sum_dices = sum(rnd.randint(1,7,4))
        # sum_dices = random.randint(2,12)
        if sum_dices <= 9:
            vygrash = vygrash + 10
        if vygrash <= 0:
            break
    return vygrash


x = np.arange(10 , 1000, 10)
vygrash1 = prob(test_num)
print (vygrash1)

plt.plot( x, vygrash1, 'r--',
         linewidth=3.0)
plt.title("Kilkist igor vs vygrash")
plt.legend("Виграш")
plt.xlim(10,1000)
plt.ylim(0, 10000)
plt.show()



