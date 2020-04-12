from django.shortcuts import render

from .models import NIR

from .forms import NIRForm

from .filters import NIRFilter

from django.views.generic.edit import DeleteView

from django.http import HttpResponseRedirect

from django.urls import reverse
from django.urls import reverse_lazy

from django.core.paginator import Paginator

from django.shortcuts import get_object_or_404

from django.db import transaction


def nir_list(request):
    f = NIRFilter(request.GET, queryset=NIR.objects.all().order_by('-pk'))
    paginator = Paginator(f.qs, 50)
    page = request.GET.get('page')
    nirs = paginator.get_page(page)
    return render(request, 'nir/nir_list.html', {'list': nirs,
                                                                  'filter': f,
                                                                  })


@transaction.atomic
def nir_add(request):
    if request.method == 'POST':
        form = NIRForm(request.POST)
        if form.is_valid():
            nir = form.save()
            for author in nir.authors.all():
                nir.subdivisions.add(author.subdivision)
            nir.leader_subdivision = nir.nir_leader.subdivision
            nir.save()
            return HttpResponseRedirect(reverse('nir:list'))
        else:
            return render(request, 'nir/nir_input_form.html', {'form': form})
    else:
        form = NIRForm
        return render(request, 'nir/nir_input_form.html', {'form': form})


@transaction.atomic
def nir_update(request, nir_id):
    if request.method == 'POST':
        obj = get_object_or_404(NIR, pk=nir_id)
        form = NIRForm(request.POST, instance=obj)
        if form.is_valid():
            nir = form.save()
            nir.subdivisions.clear()
            for author in nir.authors.all():
                nir.subdivisions.add(author.subdivision)
            nir.leader_subdivision = nir.nir_leader.subdivision
            nir.save()
            return HttpResponseRedirect(reverse('nir:list'))
        else:
            return render(request, 'nir/nir_update_form.html', {'form': form})
    else:
        obj = get_object_or_404(NIR, pk=nir_id)
        form = NIRForm(instance=obj)
        return render(request, 'nir/nir_update_form.html', {'form': form,
                                                           'obj': obj,
                                                           })


class NIRDelete(DeleteView):
    model = NIR
    success_url = reverse_lazy('nir:list')
