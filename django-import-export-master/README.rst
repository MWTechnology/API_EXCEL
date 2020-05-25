====================
django-import-export(переделаена для API яндекс карт)
====================
Чтобы установить программу на свой компьютер:
Требутся python (ссылка на скачивание https://drive.google.com/open?id=1lrZPrwIdGrVY7RCLy_mWRHeuE6V9r90i )

PyCharm( ссылка на скачивание https://drive.google.com/open?id=1Tl1HJlt92f1hVOIplNMR5QIoOJtxoNLN )

И сам репозиторий 

После установки python и PyCharm 

1) Создаём проект 

2) Клонируем в наш проект папку с Github

3)Переходим к необходимой папке cd API_EXCEL-master/django-import-export-master/tests

4)pip install -r requirement_excel.txt (Устанавливаем необходимые библиотеки)

5) вводим по порядку команды 

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

admin

пропуск (или любой email)  Это не важно
пароль 
ещё раз пароль 

python manage.py runserver

6) переходим по ссылке http://127.0.0.1:8000/admin/

7) далее books -> импортировать (обратите внимание какая должна быть таблица Excel (там указаны названия столбцов)

8)



