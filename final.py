username=input('Введите Ваше Имя: ')
content=input('Введите описание заметки: ')
status=input('Введите статус заметки: ')
created_date=input('Введите дату создания (дд.мм.гг.): ')
issue_date=input('Введите дату окончания (дд.мм.гг.): ')
title=[]
for i in range (3):
    x=input('Введите заголовок: ')
    title.append(x)
values=[username,content,status,created_date,issue_date,title]
key_note=["Имя пользователя ","Описание заметки ","Статус заметки ","Дата создания ","Дата окончания ", 'titles']
note=dict(zip(key_note,values))
print('Имя пользователя - ',note["Имя пользователя "])
print('Описание заметки - ',note["Описание заметки "])
print('Статус заметки - ',note["Статус заметки "])
print('Дата создания - ',note["Дата создания "])
print('Дата окончания - ',note ["Дата окончания "])
print('Список заголовков: ',note['titles'])
