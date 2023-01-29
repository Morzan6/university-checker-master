import os, django
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
import asyncio
from user_model.models import User


async def add_service(user_login, service):  # Добавляет сервис
    user = User.objects.get(tgid=user_login)
    subs = user.subscribes
    subs = subs + " " + service + ","
    user.subscribes = subs
    user.save()


async def remove_service(user_login, service):  # Удаляет сервис
    user = User.objects.get(tgid=user_login)
    subs = user.subscribes
    subs = subs.split(service+",")
    subs = str(subs[0]+subs[1])
    print(subs)
    user.subscribes = subs
    user.save()



asyncio.run(add_service(975083397, "bmstu"))