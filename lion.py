from collections import Counter as ct
from docx import Document as dc
from string import punctuation as pcc
import matplotlib.pyplot as plt
import pandas as pd
from openpyxl import Workbook 
import string

doc = dc('lion.docx')#Создание переменной с файлом
text_f = []#Финальная версия набора слов из документа
text_s = []#Изначальная версия
text_p = []#Промежуточная версия 

'''Частотный список'''

pc = pcc + '—'#Создание строки с неугодными знаками препинания 

for docparagraph in doc.paragraphs:#Файл в список
    text_s.append(docparagraph.text)

text_s = ''.join(text_s)#Список в строку
text_s = text_s.lower()#Все слова с маленькой буквы для правильного подсчёта 

for i in text_s:
    if i not in pc:
        text_p.append(i)#Фильтруем на негуодные знаки припенания 
    else:
        text_p.append(' ')#Вместо них пробелы

text_p = ''.join(text_p)#В строку 

text_f = text_p.split()#Делим по пробелу(для избежания ошибок в определении слов)

text_len = len(text_f)#Кол-во всех слов

ish = ct(text_f)

'''Представление в виде таблицы'''


wb = Workbook()  #Создание Excel-файла
ws = wb.active
ws.title = "Частотный список"


ws.append(["Слово", "Количество", "Процент"]) #Записываем заголовки таблицы


for nas, zn in ish.items():  #Заполняем таблицу
    prc = (zn / text_len) * 100
    ws.append([nas, zn, f"{prc:.2f}%"])


wb.save('GryobanayaTablitsa.xlsx')  #Сохраняем файл


'''График'''

let = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц','ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я']
ish_let = {}

str_f = ''.join(text_f)
ish_f = ct(str_f)

for i, j in ish_f.items():
    if i in let:
        ish_let[i] = j

sort_let = sorted(ish_let.keys())
plot_v = [ish_let[letter] for letter in sort_let]

#создание графика
plt.figure(figsize=(12, 6))
plt.bar(sort_let, plot_v, color='coral')
plt.xlabel('Буквы')
plt.ylabel('Количество')
plt.title('График частоты встречи букв')
plt.grid(axis='y')

# Отображаем график
plt.tight_layout()
plt.show()
