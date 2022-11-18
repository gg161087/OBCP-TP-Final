from django.shortcuts import render
from .models import *

def index(request):
    num_films = Film.objects.all().count()
    num_instances = FilmInstance.objects.all().count()
    num_authors = Author.objects.all().count()

    available = FilmInstance.objects.filter(status__exact='a').count()
    
    return render(
        request,
        'index.html',
        context={
            'num_films': num_films,
            'num_instances': num_instances,
            'num_authors': num_authors,
            'available': available
        }
    )