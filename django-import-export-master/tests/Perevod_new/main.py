#Импортируем библиотеку(Которую заранее установили через pip install)
# т.е вам надо в командной строке ввести
# pip install xlrd
# pip install xlwt
# pip install yandex_geocoder
# далее всё должно происходить в одной папке (т.е и сама программа и excel файл будут в одной папке)
import xlrd, xlwt
from decimal import Decimal
from yandex_geocoder import Client
#вводим ключ для геокодирования адресов (это мой ключ его можно получить в кабинете разработчика яндекс)
client = Client("2ef6f488-c05f-465e-b89b-9c1b17066afc")
#открываем файл с ваше базой данных адресов
rb = xlrd.open_workbook('api2.xls')

#выбираем активный лист
sheet = rb.sheet_by_index(0)

#################################################################
#Задаём переменную для будующего создания нового файла
wb = xlwt.Workbook()
#Задаём шаблонное название страницы в Excel
ws = wb.add_sheet('1', cell_overwrite_ok=True)


#с А3 по Е3 записываем шапку
ws.write(0, 0, "id")
ws.write(0, 1, "id_people")
ws.write(0, 2, "description")
ws.write(0, 3, "latitude_home")
ws.write(0, 4, "longitude_home")
ws.write(0, 5, "latitude_other")
ws.write(0, 6, "longitude_other")
ws.write(0, 7, "work_or_other")

#запускаем цикл для сохранения данных построчно(пока что 1000 , если адресов будет больше меняете это значение
predel=1200
for a in range(0,predel):
    #это индексы строчек в excel файлах
    #(ОБЯЗАТЕЛЬНО) файлы должны быть шаблонные
    a +=1#для исходного файла
    i=a#ля файла который создаётся
    #try и except я использую для избежания ошибки вызывающейся при попадании на пустую строку в Excel
    try:
        #Дастаём значение из строчки
        val = sheet.row_values(a)[0]
        #записываем их в новый файл(вот это именно подпись точки) я её заменю на пустую строчку
        #ws.write(i, 3, val)
        #ws.write(i, 3, " ")
        ws.write(i, 0, str(int(val)))
    except IndexError:
        pass
    try:
        # Дастаём значение из строчки
        vald = sheet.row_values(a)[5]
        valc = sheet.row_values(a)[4]
        valf = sheet.row_values(a)[7]
        #то что будет храниться в описание
        opis = str(vald)+"("+str(valc)+")-"+str(valf)
        ws.write(i, 2, opis)
    except IndexError:
        pass
    try:
        # Дастаём значение из строчки

        vale = sheet.row_values(a)[6]
        coordinates = client.coordinates(vale)
        #Долгота
        ws.write(i, 4, coordinates[0])
        # Широта
        ws.write(i, 3, coordinates[1])
        i2=i
        print(i)
    except IndexError:
        pass
#здесь я поставлю комментарий но если вы захотите показывать все адреса уберёте ковычки """
# тут и ...


#z=i2
for a in range(0,predel):
    a +=1

    z=a
    try:
        val = sheet.row_values(a)[2]
        ws.write(z, 1, str(int(val)))

    except IndexError:
        pass
    try:
        vale = sheet.row_values(a)[8]
        if vale == '':
            ws.write(z, 7, 'other')
            print(z, '-ошибка')
        else:
            coordinates = client.coordinates(vale)

            # Долгота
            ws.write(z, 6, coordinates[0])
            # Широта
            ws.write(z, 5, coordinates[1])
            i3 = z
            print(z)
    except IndexError:
        pass

z=i3
for a in range(0, predel):
    a +=1
    z=a
    try:
        vale = sheet.row_values(a)[9]
        if vale == '':
            ws.write(z, 7, 'work')
            print(z, '-ошибка')
        else:
            coordinates = client.coordinates(vale)

            # Долгота
            ws.write(z, 6, coordinates[0])
            # Широта
            ws.write(z, 5, coordinates[1])
            i2 = z
            print(z)


    except IndexError:
        pass
# и тут

#сохраняем рабочую книгу для дальнейшего использования
wb.save('geokoders.xls')
