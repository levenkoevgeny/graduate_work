from django.shortcuts import render, get_object_or_404

from .models import DissertationResearch

from .forms import DissertationResearchForm

from .filters import DissertationResearchFilter

from django.views.generic.edit import DeleteView

from django.http import HttpResponseRedirect

from django.urls import reverse
from django.urls import reverse_lazy

from django.core.paginator import Paginator

from django.db import transaction


def dissertation_research_list(request):
    f = DissertationResearchFilter(request.GET, queryset=DissertationResearch.objects.all().order_by('-pk'))
    paginator = Paginator(f.qs, 50)
    page = request.GET.get('page')
    dissertations = paginator.get_page(page)
    return render(request, 'dissertationresearch/dissertation_list.html', {'list': dissertations,
                                                                           'filter': f,
                                                                           })


@transaction.atomic
def dissertation_research_add(request):
    if request.method == 'POST':
        form = DissertationResearchForm(request.POST)
        if form.is_valid():
            dissertation = form.save()
            dissertation.research_place_subdivision = dissertation.author.subdivision
            dissertation.leader_subdivision = dissertation.leader.subdivision
            dissertation.save()
            return HttpResponseRedirect(reverse('dissertation:list'))
        else:
            return render(request, 'dissertationresearch/dissertation_input_form.html', {'form': form})
    else:
        form = DissertationResearchForm
        return render(request, 'dissertationresearch/dissertation_input_form.html', {'form': form})


@transaction.atomic
def dissertation_research_update(request, dissertation_research_id):
    if request.method == 'POST':
        obj = get_object_or_404(DissertationResearch, pk=dissertation_research_id)
        form = DissertationResearchForm(request.POST, instance=obj)
        if form.is_valid():
            dissertation = form.save()
            dissertation.research_place_subdivision = dissertation.author.subdivision
            dissertation.leader_subdivision = dissertation.leader.subdivision
            dissertation.save()
            return HttpResponseRedirect(reverse('dissertation:list'))
        else:
            return render(request, 'dissertationresearch/dissertation_update_form.html', {'form': form})
    else:
        obj = get_object_or_404(DissertationResearch, pk=dissertation_research_id)
        form = DissertationResearchForm(instance=obj)
        return render(request, 'dissertationresearch/dissertation_update_form.html', {'form': form,
                                                                                      'obj': obj,
                                                                                      })


class DissertationResearchDelete(DeleteView):
    model = DissertationResearch
    template_name = 'dissertationresearch/dissertation_confirm_delete.html'
    success_url = reverse_lazy('dissertation:list')
