from django.core.validators import RegexValidator

name_validator = RegexValidator("^[A-ZА-Я]{1,1}[A-Za-zА-Яа-яЁё,-]{0,}", message="Введите корректное значение в поле - Фамилия")
