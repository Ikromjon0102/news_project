from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import Profile


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username=data['username'],
                                password=data['password'])

            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Muvaffaqiyatli login amalga oshirildi!')
                else:
                    return HttpResponse('Sizning profilingiz faol holatda emas')

            else:
                return HttpResponse('Login va parolda xatolik bor!')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {"form": form})


@login_required
def profile_view(request):
    user = request.user
    context = {
        'user': user,
    }

    return render(request, 'pages/user_profile.html', context)

