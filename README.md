# **api_yatube_final**
### **Описание**
Социальная сеть блогеров. **Учебный проект**.

Сообщество для публикаций. Блог с возможностью публикации постов, подпиской на группы и авторов, а также комментированием постов посредством использования API.<br/>
(без фронтенда)

### **Стек**
![python version](https://img.shields.io/badge/Python-3.7-green)
![django version](https://img.shields.io/badge/Django-2.2-green)
![djangorestframework version](https://img.shields.io/badge/DRF-3.12-green)
![djoser version](https://img.shields.io/badge/djoser-2.1-green)
![simplejwt version](https://img.shields.io/badge/DRFsimplejwt-4.7-green)

### **Запуск проекта в dev-режиме**
Инструкция ориентирована на операционную систему windows и утилиту git bash.
Для прочих инструментов используйте аналоги команд для вашего окружения.

1. Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone https://github.com/Banes31/api_final_yatube-1.git
```

```
cd api_final_yatube
```

2. Установите и активируйте виртуальное окружение
```
python -m venv venv
``` 
```
source venv/Scripts/activate
```

3. Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```

4. В папке с файлом manage.py выполните миграции:
```
python manage.py migrate
```

5. В папке с файлом manage.py запустите сервер, выполнив команду:
```
python manage.py runserver
```

### Подробную документацию с примерами запросов и ответов на них вы найдете по адресу:
http://127.0.0.1:8000/redoc/

### **Автор**
[Иван Зоренко](https://github.com/Banes31)
