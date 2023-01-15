## Git
#### 1. Создать ветку lesson_8 от develop
#### 2. Все задания делаем в ветке lesson_8
#### 3. Создать MR lesson_8 -> develop и отправить ментору на ревью

## Django
#### 1. Добавляем новый application - apps/dialogs - заготовка для чата:
+ добавляем модели Thread + Message
```python
    class Thread(models.Model):
        participants = models.ManyToManyField(???)
        created_at = ???
        updated_at = ???
    
    class Message(models.Model):
        text = models.TextField()
        sender = ???
        thread = ???
        created_at = ???
        updated_at = ???
        is_read: bool = False
```  
+ заполняем файл admin.py + поиск
#### 2. Сделать для модели Message кастомный MessageManager:
+ Message.objects.read() - вывод прочтенных
+ Message.objects.unread() - вывод не прочтенных
#### 3. Добавить дата миграцию (создает 2 User'ов, создаем один тред, и несколько сообщений, сообщения создаем c помощью bulk_create)
#### 4. Попробуйте в шеле запросы с фильтрами, агрегацией и анотацией
#### 5. В lesson.md в секции "На почитать" информация которая поможет вам разобраться с менеджарми и различными запросами
#### 6. В проекте how_to_django в файле settings.py есть настройки логов.
