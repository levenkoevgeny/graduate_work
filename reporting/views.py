from django.shortcuts import render, get_object_or_404
from authors.models import Author, Subdivision
from nir.models import NIR
from sciencework.models import Publicationkind, Grif, Magazine
from reporting.models import RatingEmployee, RatingTableEmployee, RatingTableSubdivision
import datetime


def employee(request):
    if 'employee_id' in request.GET:
        author = get_object_or_404(Author, pk=request.GET['employee_id'])
        publication_list = author.sciencework_set.all().filter(year__gte=request.GET['year_since']).filter(
            year__lte=request.GET['year_till']).order_by('year', 'kind__publicationkind')

        nir_list = NIR.objects.filter(start_date__year__lte=request.GET['year_till']).exclude(end_date__year__lt=request.GET['year_since'])
        nir_list_author = nir_list.filter(authors=author)
        nir_list_leader = nir_list.filter(nir_leader=author)
        nir_list_author.union(nir_list_leader)

        anr_list = author.anr_set.all().filter(year__gte=request.GET['year_since']).filter(
            year__lte=request.GET['year_till'])
        datenow = datetime.datetime.now().date()
        date1 = author.position_date
        delta = datenow - date1
        deltadays = delta.days
        if deltadays <= 31:
            d = deltadays
            suf = 'день(дней)'
        elif deltadays > 31 and deltadays < 365:
            d = round((deltadays / 30), 1)
            suf = 'месяца(месяцев)'
        else:
            d = round((deltadays / 365), 1)
            suf = 'года(лет)'
        year_since = int(request.GET['year_since'])
        year_till = int(request.GET['year_till'])
        year_list = list()
        while year_since <= year_till:
            year_list.append(str(year_since))
            year_since = year_since + 1
        return render(request, 'reporting/employee_report.html', {'author': author,
                                                                  'publicationlist': publication_list,
                                                                  'd': d,
                                                                  'suf': suf,
                                                                  'year_list': year_list,
                                                                  'year_till': request.GET['year_till'],
                                                                  'year_since': request.GET['year_since'],
                                                                  'nir_list': nir_list_author,
                                                                  'anr_list': anr_list,
                                                                   })
    else:
        return render(request, 'reporting/employee_report.html', {
        })


def subdivision(request):
    if 'subdivision_id' in request.GET:
        subdivision = Subdivision.objects.get(pk=request.GET['subdivision_id'])
        publication_list = subdivision.sciencework_set.all().filter(year__gte=request.GET['year_since']).filter(
            year__lte=request.GET['year_till']).order_by('year', 'kind__publication_kind')
        nir_list = subdivision.nir_set.all().filter(start_date__year__gte=request.GET['year_since']).filter(
            start_date__year__lte=request.GET['year_till'])
        anr_list = subdivision.anr_set.all().filter(year__gte=request.GET['year_since']).filter(
            year__lte=request.GET['year_till'])
        year_since = int(request.GET['year_since'])
        year_till = int(request.GET['year_till'])
        year_list = list()
        while year_since <= year_till:
            year_list.append(str(year_since))
            year_since = year_since + 1
        return render(request, 'reporting/subdivision_report.html', {
            'subdivision': subdivision,
            'publication_list': publication_list,
            'nir_list': nir_list,
            'anr_list': anr_list,
            'year_till': request.GET['year_till'],
            'year_since': request.GET['year_since'],
            'year_list': year_list,
        })
    else:
        return render(request, 'reporting/subdivision_report.html')


def magazines(request):
    return render(request, 'reporting/magazines.html')


def sciencetific_activities(request):
    return render(request, 'reporting/scientific_activities.html')


def employee_rating(request):
    if 'employee_id' in request.GET:
        id = request.GET['employee_id']
        rating_author = get_object_or_404(Author, pk=id)
        rating = make_rating(id)

        return render(request, 'reporting/employee_rating.html',
                      {
                          'author': rating_author,
                          'rating': str(rating),
                      })
    else:
        return render(request, 'reporting/employee_rating.html')


def employee_rating_table(request):
    if request.method == 'GET':
        rating_list = RatingTableEmployee.objects.all().order_by('place')
        return render(request, 'reporting/employee_rating_table.html',
                      {
                          'rating_list': rating_list,
                      })
    elif request.method == 'POST':
        RatingTableEmployee.objects.all().delete()
        authors_list = Author.objects.all()
        for author in authors_list:
            rating_table_row = RatingTableEmployee(
                author=author,
                rating=make_rating(author.id),
                place=1,
            )
            rating_table_row.save()

        rating_list = RatingTableEmployee.objects.all().order_by('-rating')
        place = 1
        rating_row_first = rating_list.first()
        rating_row_first.place = place
        rating_row_first.save()
        rating_list_other = rating_list.exclude(author=rating_row_first.author).order_by('-rating')
        for rating_row in rating_list_other:
            if rating_row.rating != rating_row_first.rating:
                place = place + 1
                rating_row.place = place
                rating_row.save()
            else:
                rating_row.place = place
                rating_row.save()
            rating_row_first = rating_row
        rating_list = RatingTableEmployee.objects.all().order_by('place')
        return render(request, 'reporting/employee_rating_table.html',
                      {
                          'rating_list': rating_list,
                      })


def subdivision_rating(request):
    if 'subdivision_id' in request.GET:
        id = request.GET['subdivision_id']
        rating_subdivision = get_object_or_404(Subdivision, pk=id)
        rating = make_subdivision_rating(id)

        return render(request, 'reporting/subdivision_rating.html',
                      {
                          'subdivision': rating_subdivision,
                          'rating': str(rating),
                      })
    else:
        return render(request, 'reporting/subdivision_rating.html')


def subdivision_rating_table(request):
    if request.method == 'GET':
        rating_list = RatingTableSubdivision.objects.all().order_by('place')
        return render(request, 'reporting/subdivision_rating_table.html',
                      {
                          'rating_list': rating_list,
                      })
    elif request.method == 'POST':
        RatingTableSubdivision.objects.all().delete()
        for subdivision in Subdivision.objects.all():
            rating_table_row = RatingTableSubdivision(
                subdivision=subdivision,
                rating=make_subdivision_rating(subdivision.id),
                place=1,
            )
            rating_table_row.save()
        rating_list = RatingTableSubdivision.objects.all().order_by('-rating')
        place = 1
        rating_row_first = rating_list.first()
        rating_row_first.place = place
        rating_row_first.save()
        rating_list_other = rating_list.exclude(subdivision=rating_row_first.subdivision).order_by('-rating')
        for rating_row in rating_list_other:
            if rating_row.rating != rating_row_first.rating:
                place = place + 1
                rating_row.place = place
                rating_row.save()
            else:
                rating_row.place = place
                rating_row.save()
            rating_row_first = rating_row
        rating_list = RatingTableSubdivision.objects.all().order_by('place')
        return render(request, 'reporting/subdivision_rating_table.html',
                      {
                          'rating_list': rating_list,
                      })


def make_subdivision_rating(id):
    subdivision_rating = 0
    subdivision = get_object_or_404(Subdivision, pk=id)
    for author in subdivision.author_set.all():
        subdivision_rating = subdivision_rating + make_rating(author.id)
    try:
        author_count = subdivision.author_set.count()
        return round(subdivision_rating/author_count, 1)
    except ZeroDivisionError:
        return 0


def make_rating(id):
    # rating_author = get_object_or_404(Author, pk=id)
    # rating = 0
    # year = RatingEmployee.objects.get(pk=1).value
    #
    # # Раздел 1 Защита диссертации
    #
    # if rating_author.candidatedate is not None:
    #     if rating_author.candidatedate.year == year:
    #         rating = rating + RatingEmployee.objects.get(pk=2).value
    #
    # if rating_author.doctordate is not None:
    #     if rating_author.doctordate.year == year:
    #         rating = rating + RatingEmployee.objects.get(pk=3).value
    #
    # # Раздел 2 Подготовка кандидата или доктора наук
    #
    # disser_list_candidate = Dissertationresearch.objects.filter(leadersemployees=rating_author).filter(
    #     dateprotect__year=year)
    #
    # rating = rating + RatingEmployee.objects.get(pk=4).value * disser_list_candidate.count()
    #
    # disser_list_doctor = Dissertationresearch.objects.filter(leadersemployees=rating_author).filter(
    #     author__isnull=False).filter(author__doctordate__year=year)
    # rating = rating + RatingEmployee.objects.get(pk=5).value * disser_list_doctor.count()
    #
    # # Раздел 3 Работа в специализированных советах
    #
    # сouncil_list = Otherkind.objects.filter(activity_id=5).filter(authors=rating_author).filter(other_year=year)
    #
    # for council in сouncil_list.filter(сouncil__category_id=1):
    #     if council.completed_work_council_id == 1 or council.completed_work_council_id == 6:
    #         rating = rating + RatingEmployee.objects.get(pk=6).value
    #     else:
    #         rating = rating + RatingEmployee.objects.get(pk=7).value
    #
    # for council in сouncil_list.filter(сouncil__category_id=2):
    #     if council.completed_work_council_id == 1 or council.completed_work_council_id == 6:
    #         rating = rating + RatingEmployee.objects.get(pk=8).value
    #     else:
    #         rating = rating + RatingEmployee.objects.get(pk=9).value
    #
    # for council in сouncil_list.filter(сouncil__category_id=3):
    #     if council.completed_work_council_id == 1 or council.completed_work_council_id == 6:
    #         rating = rating + RatingEmployee.objects.get(pk=10).value
    #     else:
    #         rating = rating + RatingEmployee.objects.get(pk=11).value
    #
    # for council in сouncil_list.filter(сouncil__category_id=4):
    #     if council.completed_work_council_id == 1 or council.completed_work_council_id == 8:
    #         rating = rating + RatingEmployee.objects.get(pk=12).value
    #     else:
    #         rating = rating + RatingEmployee.objects.get(pk=13).value
    #
    # for council in сouncil_list.filter(сouncil__category_id=5):
    #     if council.completed_work_council_id == 1:
    #         rating = rating + RatingEmployee.objects.get(pk=14).value
    #     else:
    #         rating = rating + RatingEmployee.objects.get(pk=15).value
    #
    # # Раздел 4 Экспертиза
    #
    # сouncil_list_expert = Otherkind.objects.filter(Q(activity_id=4) | Q(activity_id=9)).filter(
    #     authors=rating_author).filter(other_year=year)
    #
    # rating = rating + сouncil_list_expert.filter(dissertation_kind_id=1).count() * RatingEmployee.objects.get(
    #     pk=16).value
    # rating = rating + сouncil_list_expert.filter(dissertation_kind_id=2).count() * RatingEmployee.objects.get(
    #     pk=17).value
    #
    # # Раздел 5 Подготовка отзыва на автореферат
    #
    # сouncil_list_refer = Otherkind.objects.filter(activity_id=8).filter(
    #     authors=rating_author).filter(other_year=year)
    #
    # rating = rating + сouncil_list_refer.filter(dissertation_kind_id=1).count() * RatingEmployee.objects.get(
    #     pk=25).value
    # rating = rating + сouncil_list_refer.filter(dissertation_kind_id=2).count() * RatingEmployee.objects.get(
    #     pk=26).value
    #
    # # Раздел 6 Участие в разработке законодательных актов, концепций и т.п.
    #
    # сouncil_list_refer = Otherkind.objects.filter(activity_id=3).filter(
    #     authors=rating_author).filter(other_year=year)
    #
    # rating = rating + сouncil_list_refer.count() * RatingEmployee.objects.get(pk=18).value
    #
    # # Раздел 7 ПЛД
    #
    # pld_list = PLD.objects.filter(authors=rating_author).filter(registrationdate__year=year)
    #
    # evras_list = pld_list.filter(kind_id=4)
    # for evras in evras_list:
    #     rating = rating + RatingEmployee.objects.get(pk=19).value / evras.authors.count()
    #
    # rb_list = pld_list.filter(kind_id=2)
    # for rb in rb_list:
    #     rating = rating + RatingEmployee.objects.get(pk=20).value / rb.authors.count()
    #
    # racional_list = pld_list.filter(kind_id=5)
    # for racional in racional_list:
    #     rating = rating + RatingEmployee.objects.get(pk=21).value / racional.authors.count()
    #
    # programm_list = pld_list.filter(kind_id=3)
    # for programm in programm_list:
    #     rating = rating + RatingEmployee.objects.get(pk=22).value / programm.authors.count()
    #
    # demand_list = pld_list.filter(kind_id=6)
    # for demand in demand_list:
    #     rating = rating + RatingEmployee.objects.get(pk=23).value / demand.authors.count()
    #
    # # Раздел 8 Внедрение результатов научной деятельности
    #
    # anr_list = ANR.objects.filter(authors=rating_author).filter(year=year)
    #
    # for anr in anr_list:
    #     rating = rating + RatingEmployee.objects.get(pk=24).value / anr.authors.count()
    #
    # # Раздел 9 Отчет по НИР
    #
    # nir_list = NIR.objects.filter(authors=rating_author).filter(approvedate__year=year)
    #
    # for nir in nir_list:
    #     rating = rating + RatingEmployee.objects.get(pk=27).value / (nir.authors.count() + 1)
    #
    # # Раздел 10 Участие в составе редакционных коллегий
    #
    # colleg_list = Otherkind.objects.filter(activity_id=6).filter(authors=rating_author).filter(other_year=year)
    # rating = rating + RatingEmployee.objects.get(pk=28).value * colleg_list.count()
    #
    # # Раздел 11 Участие в проведении НИР в рамках международных проектов и т.д.
    #
    # nir_list_main = NIR.objects.filter(approvedate__isnull=True).filter(Q(startdate__year__lte=year) and Q(enddate__year__gte=year))
    #
    # nir_list_leader = nir_list_main.filter(leadersemployees=rating_author)
    # rating = rating + nir_list_leader.count() * RatingEmployee.objects.get(pk=41).value
    #
    # nir_list_member = nir_list_main.filter(authors=rating_author)
    # rating = rating + nir_list_member.count() * RatingEmployee.objects.get(pk=42).value
    #
    # nir_list_other = Otherkind.objects.filter(activity_id=7).filter(authors=rating_author).filter(other_year=year)
    # rating = rating + nir_list_other.count() * RatingEmployee.objects.get(pk=42).value
    #
    #
    # # Раздел 12 Модератор научного форума / руководитель секции
    #
    # conference_list_international = Conference.objects.filter(moderators=rating_author).filter(forumdate__year=year).filter(forumstatus_id=2)
    # rating = rating + RatingEmployee.objects.get(pk=29).value * conference_list_international.count()
    #
    # conference_list_republ = Conference.objects.filter(moderators=rating_author).filter(forumdate__year=year).filter(
    #     Q(forumstatus_id=1) | Q(forumstatus_id=3))
    # rating = rating + RatingEmployee.objects.get(pk=30).value * conference_list_republ.count()
    #
    # # Раздел 13 Публикационная активность
    #
    # monograph_list = Publication.objects.filter(kind_id=1).filter(authors=rating_author).filter(year=year)
    # for monograph in monograph_list:
    #     rating = rating + float(monograph.sheetcount) * RatingEmployee.objects.get(pk=31).value / monograph.authorcount
    #
    # digest_magazine_list = Publication.objects.filter(kind_id=9).filter(authors=rating_author).filter(year=year).filter(
    #     conference__isnull=True)
    #
    # for d_m in digest_magazine_list:
    #     rating = rating + RatingEmployee.objects.get(pk=44).value / d_m.authorcount
    #
    # vestnik_list = Publication.objects.filter(kind_id=9).filter(authors=rating_author).filter(year=year).filter(
    #     magazine_id=1)
    # for vestnik in vestnik_list:
    #     rating = rating + RatingEmployee.objects.get(pk=32).value / vestnik.authorcount
    #
    # VAK_list = Publication.objects.filter(kind_id=9).filter(authors=rating_author).filter(year=year).filter(
    #     Q(magazine__invak=True) | Q(digest__invak=True))
    # for vak in VAK_list:
    #     rating = rating + RatingEmployee.objects.get(pk=33).value / vak.authorcount
    #
    # scopus = get_object_or_404(InternationalBase, pk=1)
    # scopus_list = Publication.objects.filter(Q(magazine__ininternational=scopus) | Q(digest__ininternational=scopus)).filter(authors=rating_author).filter(
    #     year=year)
    # for scop in scopus_list:
    #     rating = rating + RatingEmployee.objects.get(pk=34).value / scop.authorcount
    #
    # web_of_science = get_object_or_404(InternationalBase, pk=3)
    # web_of_science_list = Publication.objects.filter(Q(magazine__ininternational=web_of_science) | Q(digest__ininternational=web_of_science)).filter(
    #     authors=rating_author).filter(
    #     year=year)
    # for web in web_of_science_list:
    #     rating = rating + RatingEmployee.objects.get(pk=35).value / web.authorcount
    #
    # rinc = get_object_or_404(InternationalBase, pk=2)
    # rinc_list = Publication.objects.filter(Q(magazine__ininternational=rinc) | Q(digest__ininternational=rinc)).filter(authors=rating_author).filter(
    #     year=year)
    # for rin in rinc_list:
    #     rating = rating + RatingEmployee.objects.get(pk=36).value / rin.authorcount
    #
    # google_scholar = get_object_or_404(InternationalBase, pk=4)
    # google_scholar_list = Publication.objects.filter(Q(magazine__ininternational=google_scholar) | Q(digest__ininternational=google_scholar)).filter(
    #     authors=rating_author).filter(year=year)
    # for g_s in google_scholar_list:
    #     rating = rating + RatingEmployee.objects.get(pk=45).value / g_s.authorcount
    #
    # periodicals_directory = get_object_or_404(InternationalBase, pk=5)
    # periodicals_directory_list = Publication.objects.filter(
    #     Q(magazine__ininternational=periodicals_directory) | Q(digest__ininternational=periodicals_directory)).filter(
    #     authors=rating_author).filter(year=year)
    # for p_d in periodicals_directory_list:
    #     rating = rating + RatingEmployee.objects.get(pk=46).value / p_d.authorcount
    #
    # digest_list = Publication.objects.filter(kind_id=9).filter(authors=rating_author).filter(year=year).filter(conference__isnull=False)
    #
    # for digest in digest_list:
    #     rating = rating + RatingEmployee.objects.get(pk=37).value / digest.authorcount
    #
    # thesis_list = Publication.objects.filter(authors=rating_author).filter(year=year).filter(Q(kind_id=10) | Q(kind_id=11))
    # for thesis in thesis_list:
    #     rating = rating + RatingEmployee.objects.get(pk=38).value / thesis.authorcount
    #
    # comment_list = Publication.objects.filter(authors=rating_author).filter(year=year).filter(kind_id=8)
    # for comment in comment_list:
    #     rating = rating + float(comment.sheetcount) * RatingEmployee.objects.get(pk=39).value / comment.authorcount
    #
    # methodological_list = Publication.objects.filter(authors=rating_author).filter(year=year).filter(kind_id=6)
    # for methodological in methodological_list:
    #     rating = rating + float(methodological.sheetcount) * RatingEmployee.objects.get(pk=40).value / methodological.authorcount
    #
    # return rating
    return 2000