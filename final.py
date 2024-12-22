
username=input('Введите Ваше Имя ')
content=input('Введите описание заметки: ')
status=input('Введите статус заметки: ')
created_date=input('Введите дату создания (дд.мм.гг.) ')
issue_date=input('Введите дату окончания (дд.мм.гг.) ')
title_list=[input('Введите заголовок 1 '), input('Введите заголовок 2 '), input('Введите заголовок 3 ')]
note=[username,content,status,created_date,issue_date,title_list]
print(note)