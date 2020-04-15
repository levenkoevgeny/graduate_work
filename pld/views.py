from django.shortcuts import render, get_object_or_404

from .models import PLD

from .forms import PLDForm

from .filters import PLDFilter

from django.views.generic.edit import DeleteView

from django.http import HttpResponseRedirect

from django.urls import reverse
from django.urls import reverse_lazy

from django.core.paginator import Paginator

from django.db import transaction

import datetime


def pld_list(request):
    f = PLDFilter(request.GET, queryset=PLD.objects.all().order_by('-pk'))
    paginator = Paginator(f.qs, 50)
    page = request.GET.get('page')
    plds = paginator.get_page(page)
    return render(request, 'pld/pld_list.html', {'list': plds,
                                                 'filter': f,
                                                 })


@transaction.atomic
def pld_add(request):
    if request.method == 'POST':
        form = PLDForm(request.POST)
        if form.is_valid():
            pld = form.save()
            for author in pld.authors.all():
                pld.subdivisions.add(author.subdivision)
            pld.date_added = datetime.datetime.now()
            pld.user_added = request.user
            pld.save()
            return HttpResponseRedirect(reverse('pld:list'))
        else:
            return render(request, 'pld/pld_input_form.html', {'form': form})
    else:
        form = PLDForm
        return render(request, 'pld/pld_input_form.html', {'form': form})


@transaction.atomic
def pld_update(request, pld_id):
    if request.method == 'POST':
        obj = get_object_or_404(PLD, pk=pld_id)
        form = PLDForm(request.POST, instance=obj)
        if form.is_valid():
            pld = form.save()
            pld.subdivisions.clear()
            for author in pld.authors.all():
                pld.subdivisions.add(author.subdivision)
            pld.date_added = datetime.datetime.now()
            pld.user_added = request.user
            pld.save()
            return HttpResponseRedirect(reverse('pld:list'))
        else:
            return render(request, 'pld/pld_update_form.html', {'form': form})
    else:
        obj = get_object_or_404(PLD, pk=pld_id)
        form = PLDForm(instance=obj)
        return render(request, 'pld/pld_update_form.html', {'form': form,
                                                            'obj': obj,
                                                            })


class PLDDelete(DeleteView):
    model = PLD
    template_name = 'pld/pld_confirm_delete.html'
    success_url = reverse_lazy('pld:list')
