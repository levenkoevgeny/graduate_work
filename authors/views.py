from django.shortcuts import render

from django.views.generic.edit import DeleteView

from django.http import HttpResponseRedirect

from django.urls import reverse
from django.urls import reverse_lazy

from django.core.paginator import Paginator

from .forms import AuthorForm

from .filters import AuthorFilter

from .models import Author

from django.shortcuts import get_object_or_404


def author_list(request):
    f = AuthorFilter(request.GET, queryset=Author.objects.all().order_by('lastname'))
    paginator = Paginator(f.qs, 50)
    page = request.GET.get('page')
    authors = paginator.get_page(page)
    return render(request, 'authors/authors_list.html', {'list': authors,
                                                         'filter': f,
                                                         })


def author_add(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return HttpResponseRedirect(reverse('authors:list'))
        else:
            return render(request, 'authors/authors_input_form.html', {'form': form})
    else:
        form = AuthorForm
        return render(request, 'authors/authors_input_form.html', {'form': form})


def author_update(request, author_id):
    if request.method == 'POST':
        obj = get_object_or_404(Author, pk=author_id)
        form = AuthorForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('authors:list'))
        else:
            return render(request, 'authors/author_update_form.html', {'form': form,
                                                                       'obj': obj,
                                                                       })
    else:
        obj = get_object_or_404(Author, pk=author_id)
        form = AuthorForm(instance=obj)
        return render(request, 'authors/author_update_form.html', {'form': form,
                                                                   'obj': obj,
                                                                   })


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors:list')
