mailing_schedule - проста програма для відправлення розсилок за графіком.

Розсилка містить спільний текст та завдання за варіантами у окремих файлах. 
Може бути застосована для відправлення варіантів завдань модульної контрольної роботи або екзаменаційних завдань.

У даному каталозі розміщено варіант для модульної контрольної роботи (заліку).

Конфігурацію описано у файли config.txt
параметри:

your_mail = "Your mail@gmail.com" - поштова адреса (підтримується тільки @gmail.com)
your_password = "Your app password" - 16-символьний пароль застосування (див. файл ReleaseNotes.txt)
subject_practice = "Завдання з МКР 1" - тема, буде зазначена у всіх листах для практичного завдання
practice_date_time = "07.06.2022 09:40" -  дата та час розсилки практичного завдання
as_attachment = 0|1	- чи треба вкладати файли з завданням як вкладення (0 - означає, що завдання - це просто текст)
files_path = "files" - шлях до каталогу з файлами
results_path = "results" - шлях до каталогу, у якому будуть створені підкаталоги з результатами робіт
randomize = 0|1 - чи вибирати завдання випадковим чином, як при витягуванні білета на іспиті, якщо 0, то завдання будуть розсилатись по порядку

У каталозі з файлами мають бути:

 - папка practice для варіантів практичних завдань, містить файли практичних завдань
 - папка theory для варіантів теоретичних завдань, містить файли теоретичних завдань
У кожній з цих папок окрім файлі завдань має бути файл text.txt з текстом, який буде додаватись до кожного листа
 - group.txt - файл зі списком студентів, які мають здавати модульну контрольну роботу
Структура кожного рядка файлу така:
поштова адреса;ПІПб;
наприклад, 
	stud1@gmail.com;Студент1;
якщо після другої крапки з комою (;) йдуть будь-які символи, то цьому студенту не буде відправлено завдання (можливо цей студент отримав залік "автомат")
тобто, якщо рядок має вигляд 
	stud2@gmail.com;Студент2;*
цей студент не отримає завдання
 - recipients.txt - файл для списку поштових адрес для розсилки (поржній, будується програмою)

Під час відправленння створюється звіт - текстовий файл з номерами отримувачів та шляхами до файлів завдань (варіантів)

Запуск:

python mod_scheduler.py

Для роботи потрібен встановлений інтерпретатор python версій 3.4 - 3.7 (на інших версіях не перевірялось)
Після запуску програма очікує на визначений у конфігурації час та відправляє листи.


Друга частина - receiver.py - читає відповіді на розсилку, відправлені тією ж датою, що й розсилка, та розкладає тексти листів-відповідей, варіанти завдань та вкладення по каталогах. receiver використовує звіт, побудований scheduler, та створює підкаталоги у каталозі, вказаному у параметрі "results_path". Каталоги іменуються 001, 002 тощо, відповідно до нумерації у звіті scheduler. У кожномоу каталозі є файл з текстами з отриманого листа (листів), файл з відправленим завданням а також вкладення - результати виконання

Запуск:

python receiver.py





