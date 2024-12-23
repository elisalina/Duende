from django import forms
from .models import User

class UserRegisterForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label="Введите ФИО: ",
        widget=forms.TextInput(attrs={"placeholder": "Введите ФИО: "})
    )
    phone_number = forms.CharField(
        max_length=12,
        label="Введите номер телефона: ",
        widget=forms.TextInput(attrs={"placeholder": "Введите номер телефона: "})
    )
    email = forms.EmailField(
        label="Введите имейл: ",
        widget=forms.EmailInput(attrs={"placeholder": "Введите имейл: "})
    )
    question = forms.ChoiceField(
        choices=[("Косметический ремонт", "Косметический ремонт"), ("Капитальный ремонт", "Капитальный ремонт")],
        label="Косметический или капитальный ремонт"
    )
    comment = forms.CharField(
        label="На какую сумму рассчитываете?",
        widget=forms.Textarea(attrs={"placeholder": "Напишите комментарий"})
    )

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'email', 'question', 'comment']