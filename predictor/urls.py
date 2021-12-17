

from django.urls import path

from predictor.views import PredictionAPIView
urlpatterns = [

    path('predict', PredictionAPIView.as_view(), name='predict'),
]
