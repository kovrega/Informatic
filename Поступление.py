# r = {}
# l = []
# while True:
#
#
# for i in range(30):
#     stroka  = l[i].split()
#     print(stroka)
#     h = []
#     for el in stroka[1:]:
#         if not el.isdigit():
#             h.append(el)
#         else:
#             break
#
#     r[' '.join(h[:-1])] = h[-1]
#
# for k in r:
#     print(f'{r[k]} - {k}')

# pdf_path = "C:\\Users\\Andrey\\Desktop\\11.05.01 Радиоэлектронные системы и комплексы СМ5.pdf"
#

'''
1 Инженерная графика РК1 4 144 68 0 51 17 76 2 72 34 38 ДЗчт 2 72 34 38 ДЗчт
2 Иностранный язык Л2 12 432 204 0 204 0 228 2 72 34 38 Зчт 2 72 34 38 Зчт 2 72 34 38 Зчт 2 72 34 38 Зчт 2 72 34 38 Зчт 2 72 34 38 РЭкз
3 История России СГН1 4 144 104 34 70 0 40 2 72 51 21 Зчт 2 72 53 19 РЭкз
4 Социология СГН2 3 108 51 17 34 0 57 3 108 51 57 Зчт
5 Информатика ИУ7 8 288 136 17 51 68 152 5 180 85 95 Экз 3 108 51 57 Зчт
6 Аналитическая геометрия ФН12 4 144 68 34 34 0 76 4 144 68 76 РЭкз
7 Математический анализ ФН12 5 180 85 34 51 0 95 5 180 85 95 Экз
8 Введение в специальность РЛ1 1 36 17 17 0 0 19 1 36 17 19 Зчт
9 Начертательная геометрия РК1 3 108 51 17 34 0 57 3 108 51 57 Экз
10 Физическая культура и спорт ФВ 2 72 68 14 54 0 4 2 72 68 4 Зчт
11 Физика ФН4 14 504 238 102 51 85 266 4 144 68 76 Экз 5 180 85 95 Экз 5 180 85 95 Экз
12 Химия ФН5 4 144 68 34 0 34 76 4 144 68 76 РЭкз
13 Интегралы и дифференциальные уравнения ФН12 5 180 85 34 51 0 95 5 180 85 95 Экз
14 Линейная алгебра и функции нескольких переменных ФН12 3 108 68 34 34 0 40 3 108 68 40 Зчт
15 Технология конструкционных материалов РЛ6 4 144 68 51 17 0 76 4 144 68 76 Зчт
16 Основы теории цепей РЛ1 7 252 119 68 34 17 133 3 108 51 57 Зчт 4 144 68 76 Экз
17 Физические основы микроэлектроники РЛ1 2 72 34 34 0 0 38 2 72 34 38 Зчт
18 Теория поля и ряды ФН12 5 180 85 51 34 0 95 5 180 85 95 Экз
19 Уравнения математической физики и преобразования Фурье ФН12 4 144 68 34 34 0 76 4 144 68 76 Экз
20 Политология СГН3 3 108 51 17 34 0 57 3 108 51 57 Зчт
21 Радиоматериалы и радиокомпоненты РЛ1 4 144 68 51 0 17 76 4 144 68 76 Экз
22 Электродинамика и распространение радиоволн РЛ1 5 180 85 51 34 0 95 5 180 85 95 Экз
23 Теория вероятностей и случайные процессы ФН12 3 108 51 17 34 0 57 3 108 51 57 Зчт
24 Метрология и радиоизмерения РЛ1 3 108 68 34 17 17 40 3 108 68 40 Зчт
25 Электроника РЛ1 5 180 85 51 17 17 95 5 180 85 95 Экз
26 Философия СГН4 3 108 51 17 34 0 57 3 108 51 57 Зчт
27 Правоведение ЮР 3 108 51 34 17 0 57 3 108 51 57 Зчт
28 Схемотехника РЛ1 7 252 85 51 34 0 167 7 252 85 167 Экз КуР
29 Технология приборостроения РЛ6 3 108 68 68 0 0 40 3 108 68 40 Зчт
30 Радиотехнические цепи и сигналы РЛ1 5 180 102 68 17 17 78 5 180 102 78 Экз
'''
#
# # Для считывания PDF
# import PyPDF2
# # Для анализа структуры PDF и извлечения текста
# from pdfminer.high_level import extract_pages, extract_text
# from pdfminer.layout import LTTextContainer, LTChar, LTRect, LTFigure
# # Для извлечения текста из таблиц в PDF
# import pdfplumber
# # Для извлечения изображений из PDF
# from PIL import Image
# from pdf2image import convert_from_path
# # # Для выполнения OCR, чтобы извлекать тексты из изображений
# import pytesseract
# # Для удаления дополнительно созданных файлов
# import os
#
#
# def text_extraction(element):
#     # Извлекаем текст из вложенного текстового элемента
#     line_text = element.get_text()
#
#     # Находим форматы текста
#     # Инициализируем список со всеми форматами, встречающимися в строке текста
#     line_formats = []
#     for text_line in element:
#         if isinstance(text_line, LTTextContainer):
#             # Итеративно обходим каждый символ в строке текста
#             for character in text_line:
#                 if isinstance(character, LTChar):
#                     # Добавляем к символу название шрифта
#                     line_formats.append(character.fontname)
#                     # Добавляем к символу размер шрифта
#                     line_formats.append(character.size)
#     # Находим уникальные размеры и названия шрифтов в строке
#     format_per_line = list(set(line_formats))
#
#     # Возвращаем кортеж с текстом в каждой строке вместе с его форматом
#     return (line_text, format_per_line)
# # Извлечение таблиц из страницы
#
# def extract_table(pdf_path, page_num, table_num):
#     # Открываем файл pdf
#     pdf = pdfplumber.open(pdf_path)
#     # Находим исследуемую страницу
#     table_page = pdf.pages[page_num]
#     # Извлекаем соответствующую таблицу
#     table = table_page.extract_tables()[table_num]
#     return table
#
# # Преобразуем таблицу в соответствующий формат
# def table_converter(table):
#     table_string = ''
#     # Итеративно обходим каждую строку в таблице
#     for row_num in range(len(table)):
#         row = table[row_num]
#         # Удаляем разрыв строки из текста с переносом
#         cleaned_row = [item.replace('\n', ' ') if item is not None and '\n' in item else 'None' if item is None else item for item in row]
#         # Преобразуем таблицу в строку
#         table_string+=('|'+'|'.join(cleaned_row)+'|'+'\n')
#     # Удаляем последний разрыв строки
#     table_string = table_string[:-1]
#     return table_string
#
# # создаём объект файла PDF
# pdfFileObj = open(pdf_path, 'rb')
# # создаём объект считывателя PDF
# pdfReaded = PyPDF2.PdfReader(pdfFileObj)
#
# # Создаём словарь для извлечения текста из каждого изображения
# text_per_page = {}
# # Извлекаем страницы из PDF
# for pagenum, page in enumerate(extract_pages(pdf_path)):
#
#     # Инициализируем переменные, необходимые для извлечения текста со страницы
#     pageObj = pdfReaded.pages[pagenum]
#     page_text = []
#     line_format = []
#     text_from_images = []
#     text_from_tables = []
#     page_content = []
#     # Инициализируем количество исследованных таблиц
#     table_num = 0
#     first_element = True
#     table_extraction_flag = False
#     # Открываем файл pdf
#     pdf = pdfplumber.open(pdf_path)
#     # Находим исследуемую страницу
#     page_tables = pdf.pages[pagenum]
#     # Находим количество таблиц на странице
#     tables = page_tables.find_tables()
#
#     # Находим все элементы
#     page_elements = [(element.y1, element) for element in page._objs]
#     # Сортируем все элементы по порядку нахождения на странице
#     page_elements.sort(key=lambda a: a[0], reverse=True)
#
#     # Находим элементы, составляющие страницу
#     for i, component in enumerate(page_elements):
#         # Извлекаем положение верхнего края элемента в PDF
#         pos = component[0]
#         # Извлекаем элемент структуры страницы
#         element = component[1]
#
#         # Проверяем, является ли элемент текстовым
#         if isinstance(element, LTTextContainer):
#             # Проверяем, находится ли текст в таблице
#             if table_extraction_flag == False:
#                 # Используем функцию извлечения текста и формата для каждого текстового элемента
#                 (line_text, format_per_line) = text_extraction(element)
#                 # Добавляем текст каждой строки к тексту страницы
#                 page_text.append(line_text)
#                 # Добавляем формат каждой строки, содержащей текст
#                 line_format.append(format_per_line)
#                 page_content.append(line_text)
#             else:
#                 # Пропускаем текст, находящийся в таблице
#                 pass
#
#         # # Проверяем элементы на наличие изображений
#         # if isinstance(element, LTFigure):
#         #     # Вырезаем изображение из PDF
#         #     crop_image(element, pageObj)
#         #     # Преобразуем обрезанный pdf в изображение
#         #     convert_to_images('cropped_image.pdf')
#         #     # Извлекаем текст из изображения
#         #     image_text = image_to_text('PDF_image.png')
#         #     text_from_images.append(image_text)
#         #     page_content.append(image_text)
#         #     # Добавляем условное обозначение в списки текста и формата
#         #     page_text.append('image')
#         #     line_format.append('image')
#
#         # # Проверяем элементы на наличие таблиц
#         # if isinstance(element, LTRect):
#         #     # Если первый прямоугольный элемент
#         #     if first_element == True and (table_num + 1) <= len(tables):
#         #         # Находим ограничивающий прямоугольник таблицы
#         #         lower_side = page.bbox[3] - tables[table_num].bbox[3]
#         #         upper_side = element.y1
#         #         # Извлекаем информацию из таблицы
#         #         table = extract_table(pdf_path, pagenum, table_num)
#         #         # Преобразуем информацию таблицы в формат структурированной строки
#         #         table_string = table_converter(table)
#         #         # Добавляем строку таблицы в список
#         #         text_from_tables.append(table_string)
#         #         page_content.append(table_string)
#         #         # Устанавливаем флаг True, чтобы избежать повторения содержимого
#         #         table_extraction_flag = True
#         #         # Преобразуем в другой элемент
#         #         first_element = False
#         #         # Добавляем условное обозначение в списки текста и формата
#         #         page_text.append('table')
#         #         line_format.append('table')
#         #
#         #     # Проверяем, извлекли ли мы уже таблицы из этой страницы
#         #     if element.y0 >= lower_side and element.y1 <= upper_side:
#         #         pass
#         #     elif not isinstance(page_elements[i + 1][1], LTRect):
#         #         table_extraction_flag = False
#         #         first_element = True
#         #         table_num += 1
#
#     # Создаём ключ для словаря
#     dctkey = 'Page_' + str(pagenum)
#     # Добавляем список списков как значение ключа страницы
#     text_per_page[dctkey] = [page_text, line_format, text_from_images, text_from_tables, page_content]
#
# # Закрываем объект файла pdf
# pdfFileObj.close()
#
# # Удаляем созданные дополнительные файлы
# # os.remove('cropped_image.pdf')
# # os.remove('PDF_image.png')
#
# # Удаляем содержимое страницы
# result = ''.join(text_per_page['Page_0'][4])
# print(result)
#
