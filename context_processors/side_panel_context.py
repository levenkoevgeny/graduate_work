from authors.models import Author
from sciencework.models import Sciencework
from nir.models import NIR
# from pld.models import PLD
from dissertationresearch.models import DissertationResearch
from anr.models import ANR


def counts(request):

    return {'author_count': Author.objects.all().count(),
            'sciencework_count': Sciencework.objects.all().count(),
            'nir_count': NIR.objects.all().count(),
            # 'pld_count': PLD.objects.all().count(),
            'dissertation_count': DissertationResearch.objects.all().count(),
            'anr_count': ANR.objects.all().count(),
            # 'otherkindcount': Otherkind.objects.all().count(),
            # 'conference_count': Conference.objects.all().count()
            }