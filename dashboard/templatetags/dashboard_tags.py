from django import template
register = template.Library()
from dashboard.models import DashBoard

import datetime


@register.filter(name='last_activity')
def last_activity(value, arg):
    act_list = value.filter(user_id=arg).order_by('-activity_date')
    return act_list[0].activity_date if act_list else "Нет данных"


@register.filter(name='work_count')
def work_count(value, arg):
    act_list = value.filter(user_id=arg)
    return act_list.count() if act_list else "0"


@register.filter(name='work_count_last_month')
def work_count_last_month(value, arg):
    act_list = value.filter(user_id=arg).filter(activity_date__month=datetime.datetime.now().month)
    return act_list.count() if act_list else "0"