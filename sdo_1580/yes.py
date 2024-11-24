n = 1
l = []
while n != 0:
    n = int(input())
    l.append(n)
R = int(input())

l = l[:-1]


def f(l):
    res = [str(len(l))]
    m = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] * l[j] > m and (l[i] * l[j]) % 6 == 0:
                m = l[i] * l[j]

    if m == R:
        res.append(str(R))
        res.append('yes')
        return res
    else:
        res.append(str(m))
        res.append('no')
        return res


print('\n'.join(f(l)))












# pdf_path = "C://Users//Andrey//Desktop//24.05.06, Системы управления летательными аппаратами, ИУ1 (РКТ1).pdf"
#
#
#
# # Для считывания PDF
# import PyPDF2
# # # Для анализа структуры PDF и извлечения текста
# from pdfminer.high_level import extract_pages, extract_text
# from pdfminer.layout import LTTextContainer, LTChar, LTRect, LTFigure
# # # Для извлечения текста из таблиц в PDF
# import pdfplumber
# # Для извлечения изображений из PDF
# # from PIL import Image
# # from pdf2image import convert_from_path
# # # Для выполнения OCR, чтобы извлекать тексты из изображений
# # import pytesseract
# # Для удаления дополнительно созданных файлов
# import os
#
#
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
#         # # Проверяем, является ли элемент текстовым
#         # if isinstance(element, LTTextContainer):
#         #     # Проверяем, находится ли текст в таблице
#         #     if table_extraction_flag == False:
#         #         # Используем функцию извлечения текста и формата для каждого текстового элемента
#         #         (line_text, format_per_line) = text_extraction(element)
#         #         # Добавляем текст каждой строки к тексту страницы
#         #         page_text.append(line_text)
#         #         # Добавляем формат каждой строки, содержащей текст
#         #         line_format.append(format_per_line)
#         #         page_content.append(line_text)
#         #     else:
#         #         # Пропускаем текст, находящийся в таблице
#         #         pass
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
#         # Проверяем элементы на наличие таблиц
#         if isinstance(element, LTRect):
#             # Если первый прямоугольный элемент
#             if first_element == True and (table_num + 1) <= len(tables):
#                 # Находим ограничивающий прямоугольник таблицы
#                 lower_side = page.bbox[3] - tables[table_num].bbox[3]
#                 upper_side = element.y1
#                 # Извлекаем информацию из таблицы
#                 table = extract_table(pdf_path, pagenum, table_num)
#                 # Преобразуем информацию таблицы в формат структурированной строки
#                 table_string = table_converter(table)
#                 # Добавляем строку таблицы в список
#                 text_from_tables.append(table_string)
#                 page_content.append(table_string)
#                 # Устанавливаем флаг True, чтобы избежать повторения содержимого
#                 table_extraction_flag = True
#                 # Преобразуем в другой элемент
#                 first_element = False
#                 # Добавляем условное обозначение в списки текста и формата
#                 page_text.append('table')
#                 line_format.append('table')
#
#             # Проверяем, извлекли ли мы уже таблицы из этой страницы
#             if element.y0 >= lower_side and element.y1 <= upper_side:
#                 pass
#             elif not isinstance(page_elements[i + 1][1], LTRect):
#                 table_extraction_flag = False
#                 first_element = True
#                 table_num += 1
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
# os.remove('cropped_image.pdf')
# os.remove('PDF_image.png')
#
# # Удаляем содержимое страницы
# result = ''.join(text_per_page['Page_0'][4])
# print(result)
#
