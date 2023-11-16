from django.urls import path
from marvel import views

urlpatterns = [
    path('', views.FilmList.as_view()),
]
