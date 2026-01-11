from django.shortcuts import render
from .models import journal
from django.contrib.auth import get_user_model
from PersonalInfo.models import info
from Nutrition.models import nutrition
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
    u = info.objects.get(id=1)
    q = "Consider these information about this person and give them 5-10 new food suggestions addressing their diet and health concerns. Return your answer in plaintext only. Nutrition Preferences:"+str(u.nutrition_preferences)+" || Medical Conditions: "+str(u.medical_conditions)
    objs = nutrition.objects.all()
    for obj in objs:
        q+=f"|| FOOD LOG: title:{obj.title}, type:{obj.food_drink}, date:{obj.datetime}, notes:{obj.notes}"
    from google import genai
    from django.conf import settings
    g = genai.Client()
    response = g.models.generate_content(
        model="gemini-2.5-flash", contents=q
    )
    return render(request, "suggestions.html", {"r":response.text})