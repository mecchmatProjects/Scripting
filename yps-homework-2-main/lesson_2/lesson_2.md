## Unpacking
```python
>> a, b = [1, 2]
>> a
1
>> b 
2

>> a, c = [1, 2, 3, 4, 5]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: too many values to unpack (expected 2)

>> a, *c = [1, 2, 3, 4, 5]
>> a
1
>> c
[2, 3, 4, 5]
```

## Functions
#### Simple function to play
```python
def sqrt(x: int = 10) -> int:
    """Calculate the square root of a number."""
    return x * x
```
#### Functions are objects
```python
>> sqrt(x=2)
4
>> sqrt(3)
9
>> type(sqrt)
<class 'function'>
```
#### Unpack parameters
```python
>> sqrt(*[4])
16
>> sqrt(**{"x": 5})
25
```

#### How to map
```python
>> squared = map(sqrt, range(6))

>> squared
<map object at 0x10ff8c5e0>
>> list(squared)
[0, 1, 4, 9, 16, 25]
```

#### How to know what parameters function takes (magic is here)
```
dir(sqrt)
sqrt.__annotations__
sqrt.__defaults__
sqrt.__code__.co_name
sqrt.__code__.co_argcount
sqrt.__code__.co_varnames
```

#### One more way
```python
import inspect

signature = inspect.signature(sqrt)
print(signature)
```

#### args + kwargs - positional + keyword arguments
```python
def show(*args, **kwargs):
    print(f"args -> {args}")
    print(f"kwargs -> {kwargs}")

show(4, "five", 6.0, seven=7)
>> args -> (4, 'five', 6.0)
>> kwargs -> {'seven': 7}
```
#### Unpack parameters
```python
show(*[4, "five", 6.0], **{"seven": 7})
>> args -> (4, 'five', 6.0)
>> kwargs -> {'seven': 7}
```

### Side effect
Говорят, что функция имеет побочный эффект, если она изменяет что-либо за пределами 
определения функции, например, изменение аргументов, переданных функции, или изменение 
глобальной переменной.
```python
def ref_copy_demo(x):
    print(f"x = {x}, id = {id(x)}")
    x += 45
    print(f"x = {x}, id = {id(x)}")


num = 10
print(f"before function call - num = {num}, id = {id(num)}") 
ref_copy_demo(num)
print(f"after function call - num = {num}, id = {id(num)}")

# Output 
>>> before function call - num = 10, id = 140704100632512
>>> x = 10, id = 140704100632512
>>> x = 55, id = 140704100633952
>>> after function call - num = 10, id = 140704100632512
```

## Decorators
##### Декоратор — это функция, которая позволяет обернуть другую функцию для расширения её функциональности без непосредственного изменения её кода.
#### Noob
```python
def plus_decorator(function):
    def wrapper(x):
        # Do something here
        result = function(x) + 5
        # Or here
        return result
    return wrapper
```
#### Pro
```python
def plus_decorator(function):
    def wrapper(*args, **kwargs):
        # Do something here
        result = function(*args, **kwargs) + 5
        # Or here
        return result
    return wrapper
```
#### God with parameters
```python
def minus_decorator(n: int = 1):
    def decrement(function):
        def wrapper(*args, **kwargs):
            # Do something here
            result = function(*args, **kwargs) - 2 * n
            # Or here
            return result
        return wrapper
    return decrement
```
#### Usage
```python
@plus_decorator
def plus_sqrt(x: int):
    return x * x


@minus_decorator(n=3)
def minus_sqrt(x: int):
    return x * x

if __name__ == '__main__':
    print(plus_sqrt(4))
    print(minus_sqrt(5))

    # One more example of usage decorators
    plus_sqrt = plus_decorator(plus_sqrt)
    print(plus_sqrt(4))
```

## [Scopes](https://realpython.com/python-scope-legb-rule/)
* Local
* Global
* Enclosing (or nonlocal)
* Built-in

## Classes
#### Simple class
```python
class SimpleBoy:
    name: str
    def __new__(cls, *args, **kwargs):
        print("I'm a __new__ method")
        # instance = super(SimpleBoy, cls).__new__(cls, *args, **kwargs)
        instance = super().__new__(cls, *args, **kwargs)
        return instance

    def __init__(self, *args, **kwargs):
        print("I'm a constructor")
        self._dream = kwargs.get("dream")  # protected instance variable
        self.__ssn = kwargs.get("ssn")     # private instance variable

    def __del__(self):
        print("I'm a destructor")

    def play(self):
        print("I am simple method, self - it's an instance")

    @classmethod
    def jump(cls):
        print("I am class method, cls - it's a whole class")

    @staticmethod
    def run():
        print("I am staticmethod, I'm here because I'm part of some logic")

    def _hide(self):
        print("I am protected method")

    def __gone(self):
        print("I am private method") 
```

#### A little bit of complex classes
```python
class Singer:
    def __init__(self, first_name: str, last_name: str):
        """Constructor"""
        self.first_name: str = first_name
        self.last_name: str = last_name

    def sing_song(self):
        return f"{self.first_name} {self.last_name} sings song"


class HappySinger(Singer):
    def __init__(self, first_name: str, last_name: str, happiness_level: int = 10):
        self.happiness_level: int = happiness_level
        super().__init__(first_name=first_name, last_name=last_name)

    def sing_song(self):
        singing = super().sing_song()
        return f"{singing} with happiness={self.happiness_level}"


class SadSinger(Singer):
    def __init__(self, first_name: str, last_name: str, say: str, sadness_level: int = 10, ):
        self.say: str = say
        self.sadness_level: int = sadness_level
        super().__init__(first_name=first_name, last_name=last_name)

    def sing_song(self):
        singing = super().sing_song()
        return f"{singing} with sadness={self.sadness_level} and says {self.say * self.sadness_level}"    
```

### A little bit information about Slots
```python
class SlotsClass:
    __slots__ = ('foo', 'bar')

>>> obj = SlotsClass()
>>> obj.foo = 5
>>> obj.foo
# 5
>>> obj.another_attribute = 'Elvis has left the building'
Traceback (most recent call last):
  File "python", line 5, in <module>
AttributeError: 'SlotsClass' object has no attribute 'another_attribute'
```

## Is it time to talk about [OOP](https://tproger.ru/translations/oop-principles-cheatsheet/) + [SOLID](https://medium.com/webbdev/solid-4ffc018077da)?
## What is [MRO](https://tirinox.ru/mro-python/)?
```python
class A:
    pass 

class B:
    pass

class C(A, B):
     pass
     
C.__mro__
>>> (__main__.C, __main__.A, __main__.B, object)
```
## About [Metaclasses](https://proglib.io/p/metaclasses-in-python) in Python?
