from django.shortcuts import render
from .models import info

# Create your views here.
def edit(request):
    if request.method == "GET":
        return render(request, 'editinfo.html', {'info':info.objects.get(id=1)})
    else:
        obj = info.objects.get(id=1)
        obj.name = request.POST['name']
        obj.age = request.POST['age']
        obj.height = request.POST['height']
        obj.weight = request.POST['weight']
        obj.medical_conditions = request.POST['medical']
        obj.nutrition_preferences = request.POST['food']
        obj.save()
        return render(request, 'editinfo.html', {'info':info.objects.get(id=1)})

def landing(request):
    return render(request, 'landing.html', {})