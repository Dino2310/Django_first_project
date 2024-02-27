from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('about/', views.about, name= 'about'),
    path('contacts/', views.contacts, name='contacts'),
    path("post/<str:slug>", views.post_detal, name="post")
]