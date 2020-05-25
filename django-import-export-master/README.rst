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

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Оставим не на долго наши действия и подготовим Excel файл для импорта 

1)Именно такая шапка должна быть у нашего исходного файла с названием (api2.xls) обратите внимание на формат 

0_number|	0.1_Potential_mistake_dueto_adress|	0.2_id	|1_region|	2_Age|	3_Gender|	4_Home_address	|5_Occupation|	6_Work_address|	7_Another_place_address

2) название странице должно быть (Sheet1)

3) Загружаем файл в дирректорию API_EXCEL-master/django-import-export-master/tests/Perevod_new

4)




