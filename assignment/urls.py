from django.urls import path

from . import views

app_name = "assignment"

urlpatterns = [
    path('', views.index, name='index'),
    # path('first/', views.first, name='first'),
    # path('second/', views.second, name='second'),
    # path('third/', views.third, name='third'),
]
