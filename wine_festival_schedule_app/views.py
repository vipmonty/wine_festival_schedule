from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'wine_festival_schedule_app/index.html')
