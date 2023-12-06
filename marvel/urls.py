from django.urls import path
from marvel import views

urlpatterns = [
    path('login', views.Login.as_view()),
    path('places', views.Places.as_view()),
]
