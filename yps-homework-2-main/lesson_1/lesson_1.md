# Git 
Git - cистема контроля версий — это система, записывающая изменения в файл или набор файлов в 
течение времени и позволяющая вернуться позже к определённой версии.

Важно уметь пользоваться git'ом вне зависимости, юзаете вы какую-то GUI или нет

## 1. Из чего начинается git - из папки .git
## 2. Создать репозиторий и подключить origin, .gitignore
```
git config --global user.name "Valerii Dyshlevyi"
git config --global user.email "valerii.dyshlevyi@yalantis.net"
==================================================================================================
cd existing_folder
git init
git remote add origin https://gitlab.com/valerii.dyshlevyi/python-school.git
```
## 3. Посмотреть список файлов
```
git status
git diff
git log
```
## 4. Сделать/изменить commit
```
git add .
git commit -m "Initial commit"
git commit -ammend
```
## 4. Запушить изменения на master branch
```
git push -u origin master
``` 
## 5. Создать новую ветку и перейти на нее.
```
git checkout -b develop
git branch develop
git push -u origin develop
```
## 6. Смерджить одну ветку в другую
```
git merge master
```
## 7. Resolve conflicts
```
git commit -o
```
## 8. Перейти на нужный commit
```
git checkout e5b33128
git reset --hard e5b33128 
```

# Python Data Types
https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747

#### Числа - 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
#### Строки - "Bob's", b"a\x01c", u"sp\xc4m"
#### Списки - [1, [2, "three"], 4.5], list(range(10))
#### Словари/хеш таблицы - {"food": "spam", "taste": "yum"}, dict(hours=10)
#### Кортежи - (1, "spam", 4, "boo"), tuple("spam"), namedtuple
#### Файлы - open("eggs.txt")
#### Множества - set("abc"), {"a", "b, "c"}
#### Прочие основные типы - Булевские значения, сами типы, None
#### Типы программных единиц - Функции, модули, классы
#### Типы, связанные с реализацией - Скомпилированный код, трассировки стека

#### String formatting
#### Underscore + dunder methods
 ```
 a = 146
 a.__str__
 dir(a)
 a = "pew"
 dir(a)
 ```

### Срезы в строках, списках, кортежах
### Словари
* avoid KeyError 
* update
### Python Builtins - https://docs.python.org/3/library/functions.html
### Mutable vs Immutable
```
t = ("holberton", [1, 2, 3])
t[1].append(4)
t[1] += 5
```

### Dynamic Typing
```
a = "Green"
id(a)
a = "Red"
id(a)
```