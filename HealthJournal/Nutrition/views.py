from django.shortcuts import render
from google import genai
from django.conf import settings

# Create your views here.
def seeAll(request):

    g = genai.Client()

    response = g.models.generate_content(
        model="gemini-2.5-flash", contents="write a short good morning message"
    )
    return render(request, "nutritions.html", {"gemini_response":response.text})