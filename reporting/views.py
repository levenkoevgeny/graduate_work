from django.shortcuts import render, get_object_or_404
from authors.models import Author
from nir.models import NIR
import datetime
from django.db.models import Q


def employee(request):
    author_list = Author.objects.all()
    if 'employee_id' in request.GET:
        author = get_object_or_404(Author, pk=request.GET['employee_id'])
        publicationlist = author.sciencework_set.all().filter(year__gte=request.GET['year_since']).filter(
            year__lte=request.GET['year_till']).order_by('year', 'kind__publicationkind')


        nir_list = NIR.objects.filter(start_date__year__lte=request.GET['year_till']).exclude(end_date__year__lt=request.GET['year_since'])
        # filter(start_date__year__lte=request.GET['year_till']).exclude(end_date__year__lt=request.GET['year_since'])
        # nir_list_author = nir_list.filter(authors=author)
        # nir_list_leader = nir_list.filter(nir_leader=author)
        nir_list_author = nir_list.filter(authors=author)
        nir_list_leader = nir_list.filter(nir_leader=author)
        nir_list_author.union(nir_list_leader)

        anr_list = author.anr_set.all().filter(year__gte=request.GET['year_since']).filter(
            year__lte=request.GET['year_till'])
        datenow = datetime.datetime.now().date()
        date1 = author.position_date
        delta = datenow - date1
        deltadays = delta.days
        if deltadays <= 31:
            d = deltadays
            suf = 'день(дней)'
        elif deltadays > 31 and deltadays < 365:
            d = round((deltadays / 30), 1)
            suf = 'месяца(месяцев)'
        else:
            d = round((deltadays / 365), 1)
            suf = 'года(лет)'
        year_since = int(request.GET['year_since'])
        year_till = int(request.GET['year_till'])
        year_list = list()
        while year_since <= year_till:
            year_list.append(str(year_since))
            year_since = year_since + 1
        return render(request, 'reporting/employee.html', {'author': author,
                                                           'publicationlist': publicationlist,
                                                           'd': d,
                                                           'suf': suf,
                                                           'year_list': year_list,
                                                           'year_till': request.GET['year_till'],
                                                           'year_since': request.GET['year_since'],
                                                           'nir_list': nir_list_author,
                                                           'anr_list': anr_list,
                                                           'author_list': author_list
                                                           })
    else:
        return render(request, 'reporting/employee.html', {
            'author_list': author_list
        })



