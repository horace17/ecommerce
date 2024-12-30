from django.shortcuts import render

from . models import Slider


# Create your views here.
def index(request):
    sliders = Slider.objects.all()
    return render(request, 'index.html', {'sliders': sliders})

