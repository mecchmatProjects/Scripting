## Git
#### 1. Создать ветку lesson_4 от мастера
#### 2. Создать ветку lesson_4_task от lesson_4
#### 3. Все задания делаем в ветке lesson_4_task
#### 4. Создать MR lesson_4_task -> lesson_4 и отправить ментору на ревью
#### 5. Добавить в requirements.txt следующие пакеты:
+ [PyJWT](https://pypi.org/project/PyJWT/)
+ [itsdangerous](https://pypi.org/project/itsdangerous/)
+ [black](https://pypi.org/project/black/)
+ [pytest](https://pypi.org/project/pytest/)
+ [isort](https://pypi.org/project/isort/)
#### 6. Создаем файл signers.py

## Python
#### 1. Создать класс Signer в signers.py:
+ конструктор принимает 2 аргумента - secret: str, salt: str
+ атрибуты экземпляра класса - secret: str, salt: str - protected
+ умеет зашифровать/расшифровать - payload: dict | str - c помощью pyjwt/itsdangerous
+ алгоритм шифрования - "HS256"
+ expiration для зашифрованных данных - optional
#### 2. main.py принимает:
+ обязательный аргумент secret: str
+ обязательный аргумент salt: str
+ обязательный аргумент action = encode/decode
+ обязательный аргумент using = pyjwt/itsdangerous
+ необязательный аргумент expiration = N seconds 
+ обязательный аргумент input = *.json файл  
+ обязательный аргумент output = *.json файл  
#### 3. main.py будет шифровать/расшифровывать список(5-10 элементов) данных из input.json ложить в список в output.json:
+ если данные не список - raise ParseError("Hmm, what is it?")
+ если данные expired - raise ValueError("It's too late apologize...")
+ если элемент списка не dict/str - raise LookupError("Who r u?")
#### 4. Написать тесты для класса Signer с помощью pytest - делаем директорию tests(conftest.py) по желанию


## НаПочитать
1. https://gist.github.com/sloria/7001839
2. https://towardsdatascience.com/30-python-best-practices-tips-and-tricks-caefb9f8c5f5
3. https://docs.quantifiedcode.com/python-anti-patterns/
4. https://devpractice.ru/unit-testing-in-python-part-1/   
5. https://habr.com/ru/post/426699/
