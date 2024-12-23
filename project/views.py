from django.shortcuts import render

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



def sign_up_by_django(request):
    info = {}

    if request.method == "POST":
        username = request.POST.get("username")

        if username in users:
            info["error"] = "Пользователь уже существует"
        else:
            info["success"] = f"Приветствуем, {username}!"
            users.append(username)

    return render(request, "registration_page.html", context=info)

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
