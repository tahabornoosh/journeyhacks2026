from django.shortcuts import render
from .models import journal
# Create your views here.
def seeAll(request):
    if request.method=="GET":
        return render(request, 'symptoms.html', {'journal':journal.objects.get(id=1)})
    if request.method=="POST":
        obj = journal.objects.get(id=1)
        obj.entry = request.POST['entry']
        obj.save()
        return render(request, 'symptoms.html', {'journal':journal.objects.get(id=1)})

def suggestions(request):
    return render(request, "suggestions.html", {})