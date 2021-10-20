from django.shortcuts import render


def index(request):
    template = 'site_app/page.html'
    return render(request, template)
