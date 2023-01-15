# Lesson 3

---
## 1. Flake8

---

**Flake8** — инструмент(линтер), позволяющий просканировать код проекта и
обнаружить в нем стилистические ошибки и нарушения различных конвенций кода на Python.  
Flake8 умеет работать не только с PEP 8, но и с другими правилами, к тому же поддерживает кастомные плагины.

```bash
# Install
python -m pip install flake8
# How to use?
flake8 main.py
# or
flake8 path/to/code/
```

Configuration setup.cfg:
```
[flake8]
doctests = True
max-line-length = 100
```

**Show examples of errors in main.flake8_example** 
```
flake8 lesson_3/flake8/examples.py
```

Где еще используют? 
 * pre-commit hooks
 * CI (Gitlab and other)  

**Show examples of errors in main.flake8_example**  
```
"lesson_3/ci/"
```

## 2. Comprehensions

--- 
### 2.1 List comprehension
Плюсы и минусы:
 * Сокращает код и делает его более читаемым.
 * +/- Вычисляет все значения при создании.
   * Не очень хорошая идея используя большой список.
   * Работает немного быстрее в большинстве случаев, чем for(не тратит время на итерацию и добавление в список при выполнении всего списка).   

```python
# never hear about steps
boring_data = []
for num in range(10, 21):
    if num % 2 == 0:
        boring_data.append(num)

print(boring_data)
# [10, 12, 14, 16, 18, 20]

result = [num for num in range(10, 21) if num % 2 == 0]
print(result)
# [10, 12, 14, 16, 18, 20]
```

### 2.2 Set comprehension  
```python
non_unique_numbers = (1, 2, 3, 4, 5, 1, 2, 3)
unique_numbers = set()
for number in non_unique_numbers:
   if number != 2:
      unique_numbers.add(number)

print(unique_numbers)
# {1, 3, 4, 5}

print({i for i in non_unique_numbers if i != 2})
# {1, 3, 4, 5}
```

### 2.3 Dict comprehension

```python
comprehension = {f"key_{i}": f"value_{i*i}" for i in range(3)}
# {'key_0': 'value_0', 'key_1': 'value_1', 'key_2': 'value_4'}
```

### 2.4 Generator comprehension

Плюсы и минусы:
 * +Lazy sequence
   * Каждый элемент вычисляется только тогда, когда он требует
   * Экономит память и процессор

```python
numbers = (3, 2, 1)

# List comprehension
list_data = [1.0 / x for x in numbers]
print(list_data, type(list_data))
# [0.3333333333333333, 0.5, 1.0] <class 'list'>

# Generator
gen_data = (1.0 / x for x in numbers)
print(type(gen_data))
# <class 'generator'>

for x in gen_data:
    print(x)
# 0.3333333333333333
# 0.5
# 1.0
```


## 3. Iterator  

---
**Итерируемым объектом** в Python называется любой объект, имеющий методы \_\_iter\_\_ или \_\_getitem\_\_, которые возвращают итераторы или могут принимать индексы. В итоге итерируемый объект это объект, который может предоставить нам итератор.

**Итератором** в Python называется объект, который имеет метод next (Python 2) или \_\_next\_\_. Вот и все. Это итератор.

**Итерация** — это процесс получения элементов из какого-нибудь источника, например списка. Итерация — это процесс перебора элементов объекта в цикле.

```python
class FibonacciIterator:
    def __init__(self, maximum: int = 10):
        self._a, self._b = 0, 1
        self.maximum = maximum

    def __iter__(self):
        print("It's time to return iterable object. __iter__")
        return self

    def __next__(self):
        if self._a > self.maximum:
            print("I'm tired. Time to stop")
            raise StopIteration

        value_to_be_returned = self._a
        self._a, self._b = self._b, self._a + self._b
        print(f"New value from __next__ is {value_to_be_returned}")
        return value_to_be_returned

if __name__ == "__main__":
    print("Start is here")
    iterator = FibonacciIterator(maximum=10)
    print("Generate list")
    list_from_iterator = [i for i in iterator]
    print(list_from_iterator)

```
## 4. Generator

---
**Генераторы** это итераторы, которые возвращают итератор. По которым можно итерировать только один раз.  
Генераторы можно использовать с циклом for или любой другой функцией или конструкцией, которые позволяют итерировать по объекту. В большинстве случаев генераторы создаются как функции. Тем не менее, они не возвращают значение так же как функции (т.е. через return), в генераторах для этого используется ключевое слово yield.
```python
def fibonacci_generator(n):
    a = b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b

gen = fibonacci_generator(10)
print("Type: ", type(gen))
print("Use list comprehension: ", [i for i in gen])
print("Try to print all: ", [i for i in gen])
# Type:  <class 'generator'>
# Use list comprehension:  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Try to print all:  []
```
## 5. Context Manager

---
Контекстные менеджеры это специальные конструкции, которые представляют из себя блоки кода, заключенные в инструкцию with.

```python
class ContextManager:
    def __init__(self):
        print('init method called')

    def __enter__(self):
        print('enter method called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')


if __name__ == "__main__":
    with ContextManager() as manager:
        print('with statement block')

# init method called
# enter method called
# with statement block
# exit method called
```

## 6. Descriptors

---
Дескриптор это атрибут объекта со “связанным поведением”, то есть такой атрибут, при доступе к которому его поведение переопределяется методом протокола дескриптора. Эти методы \_\_get\_\_, \_\_set\_\_ и \_\_delete\_\_. Если хотя бы один из этих методов определен в объекте, то можно сказать что этот метод дескриптор.

Whaaaaat? :)

```python
class NonNegative:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print("!!! I'm use __get__")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print("!!! I'm use __set__")
        if value < 0:
            raise ValueError('Cannot be negative.')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print("!!! I'm use __delete__")
        raise ValueError('Cannot be deleted.')
    # after python 3.6

    # ! remove
    # def __init__(self, name):
    #     self.name = name

    # ! add
    # def __set_name__(self, owner, name):
    #     self.name = name

    # balance = NonNegative()


class Wallet:
    balance = NonNegative('balance')

    @property
    def __init__(self, balance):
        self.balance = balance


john_wallet = Wallet(balance=123)
# !!! I'm use __set__

print(john_wallet.balance)
# !!! I'm use __get__
# 123

john_wallet.balance = -1
# !!! I'm use __set__
# Traceback (most recent call last):
#   File "...code.py", line 90, in runcode
#     exec(code, self.locals)
#   File "<input>", line 1, in <module>
#   File "<input>", line 12, in __set__
# ValueError: Cannot be negative.

del john_wallet.balance
# !!! I'm use __delete__
# Traceback (most recent call last):
#   File "...code.py", line 90, in runcode
#     exec(code, self.locals)
#   File "<input>", line 1, in <module>
#   File "<input>", line 17, in __delete__
# ValueError: Cannot be deleted.

```


## Reading recommendation
1. Flake8
 - https://flake8.pycqa.org/en/latest/

2. Comprehensions
 - https://realpython.com/list-comprehension-python/#when-not-to-use-a-list-comprehension-in-python 
 - https://towardsdatascience.com/comprehensions-and-generator-expression-in-python-2ae01c48fc50
 - https://ru.hexlet.io/courses/python_101/lessons/python_gens/theory_unit  

3. Iterator
 - https://realpython.com/python-for-loop/#iterables

4. Generator
 - https://realpython.com/introduction-to-python-generators/
 - https://docs.python.org/3/whatsnew/3.3.html#pep-380 

5. Context Manager  
 - https://docs.python.org/3/library/stdtypes.html#context-manager-types

6. Descriptors
 - https://webdevblog.ru/chto-takoe-deskriptory-i-ih-ispolzovanie-v-python-3-6/
 - https://realpython.com/python-descriptors/
 - https://habr.com/ru/post/122082/
 - https://habr.com/ru/post/479824/  