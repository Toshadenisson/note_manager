title=[]
while True: #-Реализован цикл, для повторных запрсов заголовков
    t_1=input('Введите заголовок. (Для завершения программы введите "стоп" или оставьте поле пустым) ')
    if len(t_1) > 0 and t_1!='стоп': #-Условие: заголовок не может быть пустым или быть равен -"стоп"
        title.append(t_1) #-В список заголовков добавляются новые заголовки.
        for i in title: # -реализован цикл, который удаляет повторяющиеся заголовки
            if int(title.count(i))>1:
                title.remove(i)
    else: # - цикл запроса заголовков прекращает работу, если поле пустое или введено "стоп"
        break
print('Заголовки заметки:')
for i in range(len(title)): # - Цикл выводит заголовки в удобном для пользователя виде
    print(f'- {title[i]}')










