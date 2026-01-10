from django.shortcuts import render,get_object_or_404
from .models import result
# Create your views here.
def showAll(request):
    objs = result.objects.all()
    return render(request, 'results.html', {'results':objs})

def show(request, slug):
    obj = result.objects.get_object_or_404(id=slug)
    return render(request, 'result.html', {'result':obj})
