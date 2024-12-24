from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegisterForm
from .models import User


def home(request):
    return render(request, "main1.html")

def registration(request):
    context = {
        "fields": {
            "ФИО": "Введите ваше ФИО: ",
            "Номер телефона": "Введите ваш номер телефона: ",
            "Email": "Введите ваш email: ",
            "Капитальный или Косметический ремонт?": "Выберите тип ремонта: ",
            "Сумма, которой вы обладаете": "Укажите сумму: ",
        }
    }
    return render(request, "registration.html", context)

def works(request):
    return render(request, "examples.html")

def about(request):
    return render(request, "about.html")

users = ["existing_user1", "existing_user2"]


def registration_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST) if 'form' in locals() else None

        if form and form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                phone_number=form.cleaned_data['phone_number'],
                email=form.cleaned_data['email'],
                question=form.cleaned_data['question'],
                comment=form.cleaned_data['comment']
            )
            user.save()

            return render(request, 'registration.html', {'success': 'Регистрация прошла успешно!'})
        return render(request, 'registration.html', {'form': form, 'error': 'Пожалуйста, исправьте ошибки в форме.'})

    else:
        form = UserRegisterForm() if 'UserRegistrationForm' in locals() else None
        return render(request, 'registration.html', {'form': form})



def sign_up_by_django(request):
    error = None
    success = None
    info = {}

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            question = form.cleaned_data['question']
            comment = form.cleaned_data['comment']

            if User.objects.filter(username=username).exists():
                error = 'Пользователь уже существует'
            else:
                User.objects.create(
                    username=username,
                    phone_number=phone_number,
                    email=email,
                    question=question,
                    comment=comment,
                )
                success = f'Приветствуем, {username}!'
        else:
            error = 'Форма заполнена неверно'

    else:
        form = UserRegisterForm()

    return render(request, 'registration_page.html', context=info)

users = ["existing_user1", "existing_user2"]

def sign_up_by_html(request):
    info = {}

    if request.method == "POST":
        username = request.POST.get("username")

        if username in users:
            info["error"] = "Пользователь уже существует"
        else:
            info["success"] = f"Приветствуем, {username}!"
            users.append(username)

    return render(request, "registration_page.html", context=info)


# Create your views here.
