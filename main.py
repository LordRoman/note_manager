# Изначальные переменные
username = 'пользователь'
title = 'заголовок'
content = 'описание'
status = 'статус'
created_date = '10-11-2024'
issue_date = '10-12-2024'

# Создаем временные переменные без года
temp_created_date = created_date[:5]  # Берем только день и месяц
temp_issue_date = issue_date[:5]      # Берем только день и месяц

# Вывод для пользователя
print(f'Имя: {username}')
print(f'Заголовок: {title}')
print(f'Описание: {content}')
print(f'Статус выполнения: {status}')
print(f'Дата создания заметки (день-месяц): {temp_created_date}')
print(f'Дата истечения заметки (день-месяц): {temp_issue_date}')