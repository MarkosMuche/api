

from django.urls import path

from aboutme.views import aboutme, index_view
urlpatterns = [

    path(route='aboutme', view=aboutme, name='aboutme'),
    path('', index_view, name='index'),
]
