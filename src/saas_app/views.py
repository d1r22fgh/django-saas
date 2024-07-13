from django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path

from visits.models import PageVisit

this_dir = Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "SAAS"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "total_page_visit": qs.count()
    }
    htmpl_template = 'home.html'
    PageVisit.objects.create(path=request.path)
    return render(request, htmpl_template, my_context)
