## Black and Isort
### black — бескомпромиссный форматтер кода

```python
# так?
def func("arg1",
         "arg2",
         kwarg="value")

# или так?
def func(
    "arg1",
    "arg2",
    kwarg="value"
)
```
### Installing

```python
 pip install black
```

### Usage 

```python
$ black .
reformatted /home/br0ke/git/pipenv/pipenv/cli/__init__.py
reformatted /home/br0ke/git/pipenv/pipenv/__init__.py
...
All done! ✨ 🍰 ✨
50 files reformatted, 11 files left unchanged. 
```

One file check 

```python 

$ black setup.py 
reformatted setup.py
All done! ✨ 🍰 ✨
1 file reformatted.
```

### Configuration
В `pyproject.toml` в корне проекта добавьте:

```yaml
[tool.black]
line-length = 100
exclude = '(\.git|\.mypy_cache|venv|migrations)'
target-version = ['py38']
```
More about [black](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html)

### Isort - меняет порядок импортов

#### Install
```python 
pip install isort
```

#### Using isort
To run on specific files:

```
isort mypythonfile.py mypythonfile2.py
```

To apply recursively:
``` 
isort .
```

## Anti Patterns vs Best Practices
### Import only that things, that you need
#### Bad
```python
from django.conf import *
```
#### Good
```python
from django.conf import settings
from apps.vehicles.models import (
    Route,
    # a lot of models that ordered alphabetical here
    Vehicle
)
```
### Import entire modules instead of individual symbols within a module. For example, 
### for a top-level module `canteen` that has a file `canteen/sessions.py`,

#### Bad
```python
from canteen import get_user  # Symbol from canteen/__init__.py
from canteen.sessions import get_session  # Symbol from canteen/sessions.py
```
#### Good
```python
import canteen
import canteen.sessions
from canteen import sessions
```

### Get value from dict structure
#### Naming

* Variables, functions, methods, packages, modules
    + `lower_case_with_underscores`
* Classes and Exceptions
    + `CapWords`
* Protected methods and internal functions
    + `_single_leading_underscore(self, ...)`
* Private methods
    + `__double_leading_underscore(self, ...)`
* Constants
    + `ALL_CAPS_WITH_UNDERSCORES`
    
### General Naming Guidelines 

Avoid one-letter variables (esp. `k`, `V`, `S`). 

*Exception*: In very short blocks, when the meaning is clearly visible from the immediate context

#### Fine, but you can spend some time and write `element`
```python
for e in elements:
    e.mutate()
```

#### Avoid redundant labeling.

#### Bad
```python
import audio

core = audio.AudioCore()
controller = audio.AudioController()
```

#### Good
```python
import audio

core = audio.Core()
controller = audio.Controller()
```

### Prefer "reverse notation".
#### Bad
```python
elements = ...
active_elements = ...
defunct_elements ...
```
#### Good
```python
elements = ...
elements_active = ...
elements_defunct = ...
```



### Avoid getter and setter methods.
#### Bad
```python
person.set_age(42)
```
#### Good
```python
person.age = 42
```

### Indentation

#### Use 4 spaces--never tabs. Enough said.

### Catch exception
#### Bad
```python
try:
    result = third_party.get("/user-profile/1")
except Exception:
# except:
    pass
```
#### Good
```python
try:
    result = third_party.get("/user-profile/1")
except third_party.TimeoutError:
    print("Too long request")
except (third_party.ParseError, third_party.DataError):
    print("Something wrong with data")
else:
    print("There are no exceptions here")
finally:
    print("End is here")
```

### Else after return/raise
#### Bad
```python
if value < 0:
    return 0
else:
    return value
```
#### Good
```python
if value < 0:
    return 0
return value
```
#### Excellent
#### Good
```python
return 0 if value < 0 else value
```

### Do not rotate condition
#### Bad
```python
if not value != 5:
    return "Yes"
```
#### Good
```python
if value == 5:
    return "Yes"
```

### Use OR operator
#### Bad
```python
return value if value else "" 
```
#### Good
```python
return value or ""
```

### Do not check that True is True and False is False =)
#### Bad
```python
if pay_condition is True and work_condition is False:
    pass
### is_good: bool
return True if is_good else False
```
#### Good
```python
if pay_condition and not work_condition:
    pass
### is_good: bool
return is_good
```

### Use tuples for conditions
#### Bad
```python
if [
    pay_condition 
    and work_condition
    and study_condition
]:
    pass
```
#### Good
```python
if (
    pay_condition 
    and work_condition
    and study_condition
):
    pass
```

и еще чуть чуть можно почитать [тут](https://docs.quantifiedcode.com/python-anti-patterns/correctness/index.html)

## Немного про pytest
