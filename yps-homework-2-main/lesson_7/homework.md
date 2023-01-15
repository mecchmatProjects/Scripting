## Git
#### 1. Создать ветку develop от master в новом репозитрии yalantis-django
#### 2. Создать ветку lesson_7 от develop
#### 3. Все задания делаем в ветке lesson_7
#### 4. Создать MR lesson_7 -> develop и отправить ментору на ревью

## Infrastructure
#### 1. Сделать так чтобы все команды с Makefile работали
#### 2. Разделить requirements на base.txt и dev.txt в папке requirements

## Django
#### 1. Создать app accounts и создать модель User:
+ унаследоваться от AbstractUser
+ сделать email обязательным полем для логина в админке(вместо username)
+ username поле сделать необязательным
+ сделать методы get_full_name() и get_age() 
#### 2. Добавить след. поля:
+ created_at
+ updated_at
+ dob: date
#### 3. Создать manager UserManager где переопределить методы:
+ create_user
+ create_superuser
#### 4. Сделать админку для модели User c возможностью:
+ добавления/удаления юзера
+ редактирования юзера
+ смены пароля для юзера


## НаПочитать - см. в lesson.md
+ ссылка на репу - https://gitlab.com/valerii.dyshlevyi/how-to-django


