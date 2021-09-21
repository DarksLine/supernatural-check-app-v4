
from django.urls import path
from .views import *

urlpatterns = [
    path('',  InitialView.as_view()),
    path('testing',  TestingView.as_view()),
    path('result',  ResultView.as_view())
]
