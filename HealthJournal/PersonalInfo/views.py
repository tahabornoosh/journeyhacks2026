from django.shortcuts import render
from .models import info

# Create your views here.
def edit(request):
    if request.method == "GET":
        return render(request, 'editinfo.html', {'info':info.objects.get(id=1)})

def landing(request):
    return render(request, 'landing.html', {})