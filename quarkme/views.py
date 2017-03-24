from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from . import models
from . import utils

# Create your views here.
def home(request):
    return render(request, 'html/index.html')


def about(request):
    return render(request, 'html/about-us.html')


def faq(request):
    return render(request, 'html/faq.html')


def contact(request):
    return render(request, 'html/contact.html')


def careers(request):
    return render(request, 'html/careers.html')


def hit(request):
    return render(request, 'html/how-it-works.html')


def terms(request):
    return render(request, 'html/t&c.html')


def login(request):
    user = utils.get_login_user(request.COOKIES)
    errors = []
    if user:
        context = {
            'user': user
        }
        return render(request, 'html/index.html', context)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        login_users = User.objects.filter(username=username)
        if len(login_users) > 0:
            login_users = login_users[0]
            if login_users.check_password(password):
                context = {
                    'user': user
                }
                res = redirect('/')
                request.session['username'] = username
                res.set_cookie(key='username', value=username, expires=0)
                return res
            else:
                errors.append("wrong password")
        else:
            errors.append("no such user found")

    return render(request, 'html/login.html', context={
        'user': None,
        'errors': errors
        })


    return render(request, 'html/login.html')


def logout(request):
    res = redirect('/')
    request.session['username'] = ''
    res.set_cookie(key='username', value='', expires=0)
    return res


def streg(request):
    return render(request, 'html/student-registration.html')


def tereg(request):
    return render(request, 'html/tutor-registration.html')
