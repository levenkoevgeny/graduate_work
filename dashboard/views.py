from django.shortcuts import render
from django.contrib.auth.models import User
from .models import DashBoard
from django.core.paginator import Paginator
from .filters import DashBoardItemFilter
from django.shortcuts import get_object_or_404


def dashboard(request):
    user_list = User.objects.all()
    dashboard_list = DashBoard.objects.all()
    return render(request, 'dashboard/dashboard.html', {'user_list': user_list,
                                                        'dashboard_list': dashboard_list
                                                        })


def dashboard_item(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    f = DashBoardItemFilter(request.GET, queryset=DashBoard.objects.filter(user_id=user.id))
    paginator = Paginator(f.qs, 50)
    page = request.GET.get('page')
    works = paginator.get_page(page)
    return render(request, 'dashboard/dashboard_item.html', {'list': works,
                                                             'filter': f,
                                                             'user_id': user_id
                                                             })