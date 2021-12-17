import pickle
from django.apps import AppConfig


class PredictorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'predictor'


filename = 'predictor/model/saved_model.sav'

loaded_model = pickle.load(open(filename, 'rb'))
