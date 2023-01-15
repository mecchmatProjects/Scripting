## Git
#### 1. Создать ветку lesson_10 - в ней и делаем домашку
#### 2. Делаем endpoints используя [Generic Views](https://www.django-rest-framework.org/api-guide/generic-views/) для Thread:
+ создание thread (2 participants only)
+ получение списка thread + particpants details
+ получение информации о thread по id
+ выхода из thread - если кол-во participants 0 - удаляем thread и сообщения
#### 3. Делаем endpoints используя функции для Message:
+ получение списка сообщений для thread
+ редактирование текста одного сообщения по id
+ пометки прочитаных сообщенией
+ создание сообщения для thread
+ удаление сообщения
#### 4. Помним про валидацию и пагинацию - да, да, надо про нее почитать.
#### 5. Сделать MR и отправить ментору на ревью
1. https://docs.djangoproject.com/en/4.0/ref/urlresolvers/
2. https://docs.djangoproject.com/en/4.0/topics/http/urls/
3. https://docs.djangoproject.com/en/4.0/topics/class-based-views/intro/
4. https://sql-academy.org/ru/trainer?sort=byId
5. https://habr.com/ru/post/483204/
6. https://www.intervolga.ru/blog/projects/relsy-veb-integratsii-rest-i-soap/
7. https://www.django-rest-framework.org/
8. https://developer.mozilla.org/ru/docs/Web/HTTP/Status
9. https://en.wikipedia.org/wiki/List_of_HTTP_status_codes