from django.shortcuts import render

from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from django.http import HttpResponseRedirect

from django.urls import reverse
from django.urls import reverse_lazy

from django.core.paginator import Paginator


def author_list(request):
    pass


def author_add(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'authors/authors_input_form.html')



class AuthorUpdate(UpdateView):
    pass


class AuthorDelete(DeleteView):
    pass

