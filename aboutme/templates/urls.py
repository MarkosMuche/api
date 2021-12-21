

from django.urls import path

from aboutme.views import aboutme
urlpatterns = [

    path('aboutme', aboutme, name='aboutme'),
]
