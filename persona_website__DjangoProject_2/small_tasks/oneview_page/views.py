from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Music, MTV, Image_Me, Image_Shooting, Now, Memory, Career, Education, Work

# Create your views here.
def oneview_page(request):
    music = Music.objects.all()
    mtv = MTV.objects.all()
    image_me = Image_Me.objects.all()
    image_shooting = Image_Shooting.objects.all()
    now = Now.objects.all()
    memory = Memory.objects.all()
    career = Career.objects.all()
    education = Education.objects.all()
    work = Work.objects.all()
    return render(request, "oneview_page/oneview_page.html",
                  {"music": music,
                   "mtv": mtv,
                   "image_me": image_me,
                   "image_shooting": image_shooting,
                   "now": now,
                   "memory": memory,
                   "career": career,
                   "education": education,
                   "work": work,
                   }
                  )
