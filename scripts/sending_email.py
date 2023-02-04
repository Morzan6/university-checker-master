import os, django
import sys 
sys.path.append('../../')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

Dict_error={
    '300': 'Затребованный url обозначает более одного ресурса, и сервер не смог однозначно определить, к какой странице url относится.',
    '301': 'Документ уже не используется сервером, а ссылка перенаправляет на другую страницу.',
    '303': 'Запрошенный ресурс находится под другим адресом и его следует запрашивать.',
    '305': 'Доступ к затребованному ресурсу может осуществляться только через прокси-сервер,',
    '307': 'Требуемый ресурс был временно переведен на другой адрес.',
    '308': 'Документ уже не используется сервером.',
    '400': 'Неверный запрос. В запросе есть синтаксическая ошибка,по причине этого запрос не может быть выполнен. Пожалуйста перепроверьте url-адрес сайта.',
    '401': 'Для доступа на эту страницу требуется авторизация на сервере.',
    '402': 'Внутренняя ошибка или ошибка конфигурации сервера.',
    '403': 'Доступ запрещён. Администратор сервера ограничил доступ к ресурсу.',
    '404': 'Страница,которую вы запросили,не найдена на сервере,по причине того,что она была удалена и более не существует.',
    '405': 'Метод, определенный в строке запроса, не дозволено применять для указанного ресурса, поэтому сервер не смог его проиндексировать.',
    '406': 'Нужный документ существует, но не в том формате.',
    '407': 'Необходима регистрация на прокси-сервере.',
    '408': 'Время запроса истекло. Пожалуйста проверьте ваше интернет-соединение. Или подождите,сайт может быть перегружен на данный момент времени.',
    '409': 'Запрос конфликтует с другим запросом или с конфигурацией сервера.',
    '410': 'Страница более не существует. Указанный url-адрес верен и не содержит ошибок,но страница была удалена.',
    '412': 'При проверке на сервере одного или более полей заголовка запроса обнаружено несоответствие.',
    '413':'Размер запроса больше, чем сервер может обоработать.',
    '414': 'Сервер отказывается обслуживать запрос, потому что запрашиваемый сервером url длиннее, чем сервер может интерпретировать.',
    '415': 'Сервер отказывается обрабатывать запрос, потому что тело запроса имеет неподдерживаемый формат.',
    '422': 'Сервер не в состоянии обработать один (или более) элемент запроса.',
    '423': 'Сервер отказывается обработать запрос, так как один из требуемых ресурсов заблокирован.',
    '424': 'Сервер отказывается обработать запрос, так как один из зависимых ресурсов заблокирован.',
    '426': 'Сервер запросил апгрейд соединения до SSL, но SSL не поддерживается клиентом.',
    '429':'Вами было отправлено слишком много запрос за короткий период времени.',
    '500': 'Внутренняя ошибка сервера.',
    '502': 'Сервер, действуя в качестве шлюза или прокси-сервера, получил недопустимый ответ от следующего сервера в цепочке запросов, к которому обратился при попытке выполнить запрос.',
    '503': 'Сервис недоступен. Возникла ошибка из-за временной перегрузки или отключения на техническое обслуживание сервера.',
    '504': 'Сервер, при работе в качестве внешнего шлюза или прокси-сервера, своевременно не получил отклик от вышестоящего сервера, к которому он обратился, пытаясь выполнить запрос.',
    '505': 'Сервер не поддерживает или отказывается поддерживать версию HTTP-протокола, которая используется в сообщении запроса робота.',
    '507': 'Сервер не может обработать запрос из-за недостатка места на диске.'
}



from models.models import Service 
from models.models import User
from django.core.mail import EmailMessage

def email_alert(service_slug,Error):
    users = User.objects.filter( subscribes__icontains = service_slug )
    service = Service.objects.get(slug = service_slug)
    print(service.name)
    for user in users: 

        email = EmailMessage(f"{service.name} - Сбой в работе сервиса.", f'Внимание, замечен сбой в {service.url}. Приносим свои извинения!\n\n{Dict_error[f"{Error}"]}', to=[user.email])
        email.send() 
email_alert('bmstu',502)    
