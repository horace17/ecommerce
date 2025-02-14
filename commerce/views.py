from django.shortcuts import render
from rest_framework.response import Response
from . serializers import MobileSerializer, WatchSerializer
from rest_framework import generics, status

from . models import Slider, Mobile, Service, Watch, Yearly, Latest, Testimonial, Subscription, Insta


# Create your views here.
def index(request):
    sliders = Slider.objects.all()
    services = Service.objects.all()
    mobiles = Mobile.objects.all()
    watches = Watch.objects.all()
    yearlys = Yearly.objects.all()
    latests = Latest.objects.all()
    testimonials = Testimonial.objects.all()
    subscriptions = Subscription.objects.all()
    instas = Insta.objects.all()

    context = {'sliders': sliders,
               'services': services,
               'mobiles': mobiles,
               'watches': watches,
               'yearlys': yearlys,
               'latests': latests,
               'testimonials': testimonials,
               'subscriptions': subscriptions,
               'instas': instas}
    return render(request, 'index.html', context)

# APIs section of Mobile model
class MobileView(generics.ListAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

# API section of Watch model
class WatchView(generics.ListAPIView):
    queryset = Watch.objects.all()
    serializer_class = WatchSerializer
