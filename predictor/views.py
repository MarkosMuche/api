from django.shortcuts import render, HttpResponse
import numpy as np
from .apps import loaded_model

from rest_framework import generics
from rest_framework.views import APIView

from .forms import HeartDataForm


class PredictionAPIView(APIView):

    def get(self, request):

        form = HeartDataForm()

        return render(request, 'predictor/predict.html', context={'form': form})

    def post(self, request):

        heart_form = HeartDataForm(request.POST)
        if heart_form.is_valid():
            l = []
           
            for key in heart_form.data.keys():
                
                if key == 'Gender':
                    if heart_form.data[key] == 'M':
                        l.append(1)
                    else:
                        l.append(0)
                else:
                    l.append(heart_form.data[key])

            arr = np.array(l[1:])

        else:
            print('not valid')

        return HttpResponse('post finished')
