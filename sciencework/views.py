from django.shortcuts import render

from django.views.generic.edit import DeleteView

from django.http import HttpResponseRedirect

from django.urls import reverse
from django.urls import reverse_lazy

from django.core.paginator import Paginator

from .models import Sciencework

from .filters import ScienceWorkFilter

from .forms import ScienceworkForm

from django.shortcuts import get_object_or_404

from django.db import transaction

import datetime


def sciencework_list(request):
    f = ScienceWorkFilter(request.GET, queryset=Sciencework.objects.all().order_by('-pk'))
    paginator = Paginator(f.qs, 50)
    page = request.GET.get('page')
    scinceworks = paginator.get_page(page)
    return render(request, 'sciencework/sciencework_list.html', {'list': scinceworks,
                                                                 'filter': f,
                                                                 })


@transaction.atomic
def sciencework_add(request):
    if request.method == 'POST':
        form = ScienceworkForm(request.POST)
        if form.is_valid():
            sciencework = form.save()
            for author in sciencework.authors.all():
                sciencework.subdivisions.add(author.subdivision)
            if sciencework.magazine is None and sciencework.digest is not None:
                sciencework.in_vak = sciencework.digest.in_vak
                for international in sciencework.digest.in_international.all():
                    sciencework.in_internationals.add(international)
            if sciencework.digest is None and sciencework.magazine is not None:
                sciencework.in_vak = sciencework.magazine.in_vak
                for international in sciencework.magazine.in_international.all():
                    sciencework.in_internationals.add(international)
            sciencework.date_added = datetime.datetime.now()
            sciencework.user_added = request.user
            sciencework.save()
            return HttpResponseRedirect(reverse('sciencework:list'))
        else:
            return render(request, 'sciencework/sciencework_input_form.html', {'form': form})

    else:
        form = ScienceworkForm
        return render(request, 'sciencework/sciencework_input_form.html', {'form': form})


@transaction.atomic
def sciencework_update(request, sciencework_id):
    if request.method == 'POST':
        obj = get_object_or_404(Sciencework, pk=sciencework_id)
        form = ScienceworkForm(request.POST, instance=obj)
        if form.is_valid():
            sciencework = form.save()
            sciencework.in_internationals.clear()
            sciencework.subdivisions.clear()
            for author in sciencework.authors.all():
                sciencework.subdivisions.add(author.subdivision)
            if sciencework.magazine is None and sciencework.digest is not None:
                sciencework.in_vak = sciencework.digest.in_vak
                for international in sciencework.digest.in_international.all():
                    sciencework.in_internationals.add(international)
            if sciencework.digest is None and sciencework.magazine is not None:
                sciencework.in_vak = sciencework.magazine.in_vak
                for international in sciencework.magazine.in_international.all():
                    sciencework.in_internationals.add(international)
            sciencework.date_added = datetime.datetime.now()
            sciencework.user_added = request.user
            sciencework.save()
            return HttpResponseRedirect(reverse('sciencework:list'))
        else:
            return render(request, 'sciencework/sciencework_input_form.html', {'form': form})
    else:
        obj = get_object_or_404(Sciencework, pk=sciencework_id)
        form = ScienceworkForm(instance=obj)
        return render(request, 'sciencework/sciencework_update_form.html', {'form': form,
                                                                            'obj': obj,
                                                                            })


class ScienceworkDelete(DeleteView):
    model = Sciencework
    success_url = reverse_lazy('sciencework:list')
