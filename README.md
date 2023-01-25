# GitHub ♥️ Django

Будем делать тут

```python
python manage.py runserver
```
 https://www.figma.com/file/ymyXt2sMhfXjmIcDzosDHr/PredProf?node-id=0%3A1&t=9gIgnzuyBXJZ8MVs-0

```
.
├── config #папка конфига с настройками 
│   ├── asgi.py
│   ├── settings.py
│   └── wsgi.py
├── core  #ядро, основная папка проекта
│   ├── apps.py
│   ├── static #папка с css и прочими статичными штуками
│   ├── templates #папка с html-шаблонами 
│   ├── urls.py  #обработчик url-запросов
│   └── views.py #функции, которые выполняет сайт при переходе на разные url
├── media #медиа файлы тут
├── scripts #папка со скриптами разными
├── raiting_model #папка с моделью рейтинга для БД
├── services_model #папка с моделью сервиса для БД
├── user_model #папка с моделью пользователя для БД
├── reports_model #папка с моделью репортов для БД
├── db.json #данные для БД
├── db.sqlite3 #база данных
├── manage.py #системный файл для работы через терминал и отправки команд
├── README.md #это для гитхаба
├── requirements.txt #необходимые библиотеки для python
└── tailwind.config.js #конфиг для тейлвинда
```

 ```
 20.01.2023 00:52
 * Добавлены сообщения об ошибках при неправильном вводе пароля или имени пользователя на signup и login
 * Закончена функция подтверждения пользователя через почту (пока работает только с yandex почтой)
 * Исправлено отображение index (главной страницы) при разных состояниях аккаунта (подтвержден/неподтвержден)
 * Исправлены баги с входом при создании нового пользователя
 ```
 ```
 21.01.2023 12:20
 * Изменена иерархия папок
 * Добавлен рендер страницы /activate из html-шаблона, с передачей инфы об успешной или неуспешной активации
 ```
 
 ```
 22.01.2023 16:00
 
 * Добавлены модели (таблицы в БД) для самого сервиса, репортов пользователей и оценок. Все расписано в фигме, что за что отвечает 
 https://www.figma.com/file/ymyXt2sMhfXjmIcDzosDHr/PredProf?node-id=0%3A1&t=9gIgnzuyBXJZ8MVs-0
 
 ```

```
23.01.2021 23:56

*Добавлена тестовая админ-панель с функцией "добавления ресурса для отслеживания его доступности" - форма с именем и url, которая летит в таблицу БД о сервисах
 соответственно обычным пользователям запрещен доступ к админ-панеле, их редиректит на главную страницу
* Исправлены модели в БД
* Добавлены новые настройки VS code в devcontainer

```

```
25.01.2023 00:37

*Добавлена возможность добавления логотипа к сервису через админ-панель
*Добавлено отображения страниц сервера по слагу с содержимым инфы об этом сервисе из БД
*Добавлена директория для медиа файлов
*Исправлены баги
```

```
26.01.2023 00:21

*Добавлена функция сообщения о недоступности ресурса
**На странице каждого сервиса есть форма для сообщения о недоступности
**Всё добавляется в БД
```