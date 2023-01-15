
 ##### Какие фреймворки есть у Python?
 ![enter image description here](https://miro.medium.com/max/1400/1*M5grT9w-wKGhOSusEpqWmw.png)
 [source](https://gustavwillig.medium.com/python-web-development-in-2021-which-web-frameworks-are-the-most-popular-by-github-stars-e07b1d7ef6f7)
 
 #### Django (Bases)
  * Почему Django стал так популярен?
  * Какие версии используем? Как скачать/установить
     https://www.djangoproject.com/download/
```bash
    pyenv local 3.10.0
    python --version
    # >>> 3.10.0
    pip install Django==3.2.11
    pip freeze >> requirements.txt
    django-admin startproject core
    django-admin help --commands
    django-admin startapp web_site
```
#### 2. Settings   
#### 3. manage.py   
#### 4. static files/media files  
#### 5. Models + admin
![Django Request & Response cycle](https://i.redd.it/jksj10krs0s31.jpg)


### Reading:
1. https://docs.djangoproject.com/en/3.2/
2. https://docs.djangoproject.com/en/3.2/intro/tutorial01/
3. http protocol - https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview
4. web sockets protocol - https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API
5. [Обзор способов и протоколов аутентификации в веб-приложениях](https://habr.com/ru/company/dataart/blog/262817/)
6. [Как работает JS: WebSocket и HTTP/2+SSE. Что выбрать?](https://habr.com/ru/company/ruvds/blog/342346/)
7. [Простым языком об HTTP](https://habr.com/ru/post/215117/)
8. [Типы HTTP-запросов и философия REST](https://habr.com/ru/post/50147/)
9. [Сравнение производительности HTTP/3 и HTTP/2](https://habr.com/ru/company/itsumma/blog/497520/)
10. [Введение в REST API — RESTful веб-сервисы](https://habr.com/ru/post/483202/)
11. [gRPC vs REST, что выбрать для нового сервера?](https://habr.com/ru/post/565020/)
12. [Балансировка нагрузки: основные алгоритмы и методы](https://habr.com/ru/company/selectel/blog/250201/)
13. [Как это работает: Пара слов о DNS](https://habr.com/ru/company/1cloud/blog/309018/)
14. [Зачем нужен Kubernetes и почему он больше, чем PaaS?](https://habr.com/ru/company/flant/blog/327338/)
15. [Docker. Зачем и как](https://habr.com/ru/post/309556/)
16. [Паттерны для новичков: MVC vs MVP vs MVVM](https://habr.com/ru/post/215605/)
17. [Apache vs Nginx: практический взгляд](https://habr.com/ru/post/267721/)
18. [Пять простых шагов для понимания JSON Web Tokens (JWT)](https://habr.com/ru/post/340146/)
