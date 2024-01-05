from django.shortcuts import render
from .models import Foydalanuvchilar


def users_list(request):
    userlar = Foydalanuvchilar.objects.all()

    context = {
        "userlar": userlar
    }

    return render(request, template_name='news/users.html', context=context)

def users_detail(request, id):
    userlar = Foydalanuvchilar.objects.get(id=id)

    context = {
        "user": userlar
    }

    return render(request, template_name='news/user_batafsil.html', context=context)
