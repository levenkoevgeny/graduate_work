from django.shortcuts import render, get_object_or_404

from .models import ANR

from .forms import ANRForm

from .filters import ANRFilter

from django.views.generic.edit import DeleteView

from django.http import HttpResponseRedirect

from django.urls import reverse
from django.urls import reverse_lazy

from django.core.paginator import Paginator

from django.db import transaction

import datetime


def anr_list(request):
    f = ANRFilter(request.GET, queryset=ANR.objects.all().order_by('-pk'))
    paginator = Paginator(f.qs, 50)
    page = request.GET.get('page')
    anrs = paginator.get_page(page)
    return render(request, 'anr/anr_list.html', {'list': anrs,
                                                 'filter': f,
                                                 })


@transaction.atomic
def anr_add(request):
    if request.method == 'POST':
        form = ANRForm(request.POST)
        if form.is_valid():
            anr = form.save()
            for author in anr.authors.all():
                anr.subdivisions.add(author.subdivision)
            anr.date_added = datetime.datetime.now()
            anr.user_added = request.user
            anr.save()
            return HttpResponseRedirect(reverse('anr:list'))
        else:
            return render(request, 'anr/anr_input_form.html', {'form': form})
    else:
        form = ANRForm
        return render(request, 'anr/anr_input_form.html', {'form': form})


@transaction.atomic
def anr_update(request, anr_id):
    if request.method == 'POST':
        obj = get_object_or_404(ANR, pk=anr_id)
        form = ANRForm(request.POST, instance=obj)
        if form.is_valid():
            anr = form.save()
            anr.subdivisions.clear()
            for author in anr.authors.all():
                anr.subdivisions.add(author.subdivision)
            anr.date_added = datetime.datetime.now()
            anr.user_added = request.user
            anr.save()
            return HttpResponseRedirect(reverse('anr:list'))
        else:
            return render(request, 'anr/anr_update_form.html', {'form': form})
    else:
        obj = get_object_or_404(ANR, pk=anr_id)
        form = ANRForm(instance=obj)
        return render(request, 'anr/anr_update_form.html', {'form': form,
                                                            'obj': obj,
                                                            })


class ANRDelete(DeleteView):
    model = ANR
    template_name = 'anr/anr_confirm_delete.html'
    success_url = reverse_lazy('anr:list')
