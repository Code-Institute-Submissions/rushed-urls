from django.shortcuts import render

# Create your views here.

"""

    View for homepage.

    route: '/'
    template: 'urlshortener/home.html'

"""
def get_home(request):
    return render(request, 'urlshortener/home.html')