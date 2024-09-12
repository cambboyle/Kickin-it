from django.shortcuts import render

# Create your views here.

def index(request):
    ''' View for the home page '''

    return render(request, 'home/index.html')