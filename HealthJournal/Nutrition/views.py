from django.shortcuts import render, redirect
from google import genai
from django.conf import settings
from .models import nutrition
from django.utils import timezone
from datetime import datetime, timedelta

# Create your views here.
def seeAll(request):

    g = genai.Client()
    objs = nutrition.objects.all()
    res = ""
    for i in objs:
        res+=f"RECORD: title:{i.title}, food_drink:{i.food_drink}, notes: {i.notes};"
    response = g.models.generate_content(
        model="gemini-2.5-flash", contents="Here is a list of the food eaten by a user. Provide a short (150 or less words) insight and new food suggestions. Use plaintext only:"+res
    )
    
    return render(request, "nutritions.html", {"gemini_response":response.text, "nutritions":objs, "count":objs.count, "date":datetime.now()})

def see(request, slug):
    if request.method=="GET":
        return render(request, 'nutrition.html', {})
    else:
        br = nutrition.objects.create(title=request.POST['m1'], food_drink=request.POST['f1'], notes=request.POST['notes'])
        lu = nutrition.objects.create(title=request.POST['m2'], food_drink=request.POST['f2'], notes=request.POST['notes'])
        di = nutrition.objects.create(title=request.POST['m3'], food_drink=request.POST['f3'], notes=request.POST['notes'])
        sn = nutrition.objects.create(title=request.POST['m4'], food_drink=request.POST['f4'], notes=request.POST['notes'])
        return redirect("/nutritions")