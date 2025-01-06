from django.urls import path

from commerce.views import MobileView

urlpatterns = [
    path('', MobileView.as_view(), name='mobile'),
]