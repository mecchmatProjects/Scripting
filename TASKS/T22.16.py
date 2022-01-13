import datetime
import time
from T228 import check


#Запуск функції перевірки кожні 10 хв
while True:
    if datetime.datetime.now().minute % 10 == 0:
        check()
    else:
        time.sleep(1000)    