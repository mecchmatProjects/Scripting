## Git
#### 1. Создать ветку lesson_2 от ветки master
#### 2. Создать ветку lesson_2_task от lesson_2
#### 3. Все задания делаем в ветке lesson_2_task
#### 4. Сделать МR lesson_2_task -> lesson_2

## Python
#### 1. Создать файлы classes.py, decorators.py и main.py
#### 2. decorators.py - создать декоратор: 
* timer, который показывает время(print) выполнения ф-ции (исп. datetime);
* update_dict с параметром N для ф-ции и если она(ф-ция) возвращает dict - то умножает каждое значение на N, если значение строка.
```python
{"a": "c", "b": 1}  # {"a": "ccc", "b": 1} если N = 3 
```

#### 3. Создать класс Employee, который:
* принимает в конструкторе 5 аргументов:
  + name: str
  + start: date - protected
  + end: date = date.today() - protected
  + rate: Decimal - protected
  + taxes: int - protected
* имеет protected атрибут balance: Decimal - для каждого instance     
* имеет метод how_long, который возвращает строку "John works 4 day(s)":
* имеет protected метод recalculate_balance для пересчёта атрибута balance
* формула расчета balance -> (end - start =  кол-во дней) * rate
* имеет метод update_rate, который принимает новый коэфициент для rate и запускает перерасчёт balance
* имеет classmethod show_header, который показывает шапку таблицы (use [format](https://www.educba.com/python-print-table/)) 
* имеет staticmethod show_line, который показывает line таблицы (use [format](https://www.educba.com/python-print-table/)) 
* имеет метод show_row, который показывает строку таблицы (use [format](https://www.educba.com/python-print-table/)) 
  + Name(исп. метод how_long)
  + Balance
  + Taxes Pay - сумма которая уйдет на налоги
  + Employee Pay - сумма которая уйдет на выплату самому employee
* validation(raise ValueError("end > start")):
  + end > start
  + 100 > rate > 10
  + 99 >= taxes > 1
  + 20 >= len(name) > 2
    
#### 4. В файле main.py сделать демо программу:
* как работает каждый декоратор
* создать список из 7 employees
* вывести их инф-цию(метод show_row)
* каждому четному employee увеличить rate в 1.5 раза 
* каждому нечетному employee увеличить rate в 3.5 раза 
* повторно вывести список employees

```
ROW_FORMAT = "| {:<30} | {:<10} | {:<10} | {:<10} |"
ROW_LENGTH = 73
-------------------------------------------------------------------------
| Name                           | Balance    | Taxes Pay  | Salary     |
-------------------------------------------------------------------------
| Mo works 576 day(s)            | 2592.0     | 648.00     | 1944.00    |
| Laura works 158400 day(s)      | 712800.0   | 356400.0   | 356400.0   |
| Sedrik works 576 day(s)        | 2592.0     | 1944.00    | 648.00     |
-------------------------------------------------------------------------
```


## НаПочитать
1. https://realpython.com/python-scope-legb-rule/
2. https://realpython.com/python-kwargs-and-args/
3. https://realpython.com/lessons/tuple-assignment-packing-unpacking/
4. https://dev.to/dev0928/what-is-a-side-effect-of-a-function-in-python-36ei
5. https://medium.com/webbdev/solid-4ffc018077da
6. https://howto.lintel.in/python-__new__-magic-method-explained/
7. https://devpractice.ru/closures-in-python/
8. https://tirinox.ru/getattribute/
