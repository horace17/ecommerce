from django.urls import path

from commerce.views import MobileView, WatchView

urlpatterns = [
    path('', MobileView.as_view(), name='mobile'),
    path('', WatchView.as_view(), name='watch'),
]