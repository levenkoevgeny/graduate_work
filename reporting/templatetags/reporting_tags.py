from django import template
from sciencework.models import Sciencework, Publicationkind
from anr.models import ANR

register = template.Library()


@register.filter(name='sciencework_count')
def sciencework_count(value, args):
    arg_list = [arg.strip() for arg in args.split(',')]
    return value.filter(kind_id=arg_list[0]).filter(year=arg_list[1]).count()


@register.filter(name='sciencework_count_subspecies')
def sciencework_count_subspecies(value, args_subspecies):
    arg_list = [arg.strip() for arg in args_subspecies.split(',')]
    return value.filter(subspecies_id=arg_list[0]).filter(year=arg_list[1]).count()


@register.filter(name='sciencework_count_grif')
def sciencework_count_grif(value, args_grif):
    arg_list = [arg.strip() for arg in args_grif.split(',')]
    return value.filter(grif_id=arg_list[0]).filter(year=arg_list[1]).count()


@register.filter(name='sciencework_count_all')
def sciencework_count_all(value, args):
    return value.filter(year=args).count()


@register.filter(name='sciencework_count_all_subspecies')
def sciencework_count_all_subspecies(value, args):
    return value.filter(subspecies_id=args).count()


@register.filter(name='sciencework_count_all_grif')
def sciencework_count_all_grif(value, args):
    return value.filter(grif_id=args).count()


@register.filter(name='sciencework_count_all_kind')
def sciencework_count_all_kind(value, args):
    return value.filter(kind_id=args).count()


@register.filter(name='sciencework_publication_all_invak')
def sciencework_publication_all_invak(value, args):
    return value.filter(kind_id=args).filter(invak=True).count()


@register.filter(name='sciencework_publication_all_not_invak')
def sciencework_publication_all_not_invak(value, args):
    return value.filter(kind_id=args).filter(invak=False).count()


@register.filter(name='sciencework_publication_invak')
def sciencework_publication_invak(value, args):
    arg_list = [arg.strip() for arg in args.split(',')]
    return value.filter(kind_id=arg_list[0]).filter(year=arg_list[1]).filter(invak=True).count()


@register.filter(name='sciencework_publication_not_invak')
def sciencework_publication_not_invak(value, args):
    arg_list = [arg.strip() for arg in args.split(',')]
    return value.filter(kind_id=arg_list[0]).filter(year=arg_list[1]).filter(invak=False).count()


@register.filter(name='anr_year')
def anr_year(value, args):
    return value.filter(other_year=args).count()


@register.filter(name='add_string')
def cut(value, arg):
    return str(value)+','+ str(arg)
