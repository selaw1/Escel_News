from django.urls import path

from . import views

app_name = "news"

urlpatterns = [
    path('', views.home_news, name='home'),
    path('sport/', views.sport_news, name='sport'),
    path('business/', views.business_news, name='business'),
    path('health/', views.health_news, name='health'),
    path('technology/', views.tech_news, name='tech'),
    path('politics/', views.politics_news, name='politics'),
    path('culture/', views.culture_news, name='culture'),
]


