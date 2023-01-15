# Lesson 5

---



## 1. When can we use a recursive generator instead of usually function?

---
	On big data, a regular recursive function is much faster to execute than a recursive generator.
	Although the linear generator execute much faster than the usual function.

	Have there ever been problems when it was necessary to use recursive generators,
	or it can use only in theory?
```python
import sys
sys.setrecursionlimit(20)
# http://pythontutor.com/visualize.html#code=def%20fib%28n%29%3A%0A%20%20%20%20print%28%22Start%3A%20%22,%20n%29%0A%20%20%20%20if%20n%20%3C%3D%201%3A%0A%20%20%20%20%20%20%20%20return%20n%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20fib%28n-1%29%20%2B%20fib%28n-2%29%0Aprint%28fib%284%29%29&cumulative=true&curInstr=47&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=true
def fib(n):
    print("Start: ", n)
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
print(fib(4))
"""
Start:  4
Start:  3
Start:  2
Start:  1
Start:  0
Start:  1
Start:  2
Start:  1
Start:  0
3
"""
```

https://habr.com/ru/post/255239/  
https://docs.python.org/3/library/pdb.html


## 2. Python Generators. send, throw

--- 
```python
def counter_generator(n: int = 5):
    for k in range(1, n + 1):
        print("Number: ", k)

        try:
            result = yield k
        except ValueError:
            result = None
            print("ValueError: ")

        if result:
            print("Additional text: ", result)
        print("-" * 10)

a = counter_generator()
next(a)
a.throw(ValueError)
next(a)
a.send(True)
next(a)
```
## 3. Metaclass
https://proglib.io/p/metaclasses-in-python
https://realpython.com/python-metaclasses/

## 4. getattr, hasattr?

---
```python
class Employee:
	name = "John"
		

e = Employee()
print(getattr(e, "name", None))

setattr(e, "last_name", "Bob")
print(e.last_name)

delattr(e, "last_name")

print(hasattr(e, "name"))

```
## 5. Где используют дескрипторы? (больше примеров)
```python
class Field:

    def __set_name__(self, owner, name):
        self.fetch = f'SELECT {name} FROM {owner.table} WHERE {owner.key}=?;'
        self.store = f'UPDATE {owner.table} SET {name}=? WHERE {owner.key}=?;'

    def __get__(self, obj, objtype=None):
        return conn.execute(self.fetch, [obj.key]).fetchone()[0]

    def __set__(self, obj, value):
        conn.execute(self.store, [value, obj.key])
        conn.commit()

class Movie:
    table = 'Movies'                    # Table name
    key = 'title'                       # Primary key
    director = Field()
    year = Field()

    def __init__(self, key):
        self.key = key

class Song:
    table = 'Music'
    key = 'title'
    artist = Field()
    year = Field()
    genre = Field()

    def __init__(self, key):
        self.key = key
```
https://docs.python.org/3/howto/descriptor.html
