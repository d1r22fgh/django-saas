from django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path

from visits.models import PageVisit

this_dir = Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        print(request.user.first_name)
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    try:
        percent = f"{round((page_qs.count() * 100.0) / qs.count(), 2)}%"
    except:
        percent = 0
    my_title = "SAAS"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        'percent': percent,
        "total_page_visit": qs.count()
    }
    html_template = 'home.html'
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)
