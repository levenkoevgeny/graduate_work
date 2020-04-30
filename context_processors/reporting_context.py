from sciencework.models import Publicationkind, Grif, Subspecies
from authors.models import Author, Subdivision


def reporting(request):

    return {'publicationkindlist': Publicationkind.objects.all(),
            'author_list': Author.objects.all(),
            'griflist': Grif.objects.all(),
            'subdivision_list': Subdivision.objects.all(),
            'subspecieslist': Subspecies.objects.all(),
            }
