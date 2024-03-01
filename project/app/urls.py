from django.urls import path
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path('', views.index, name= 'index'),
    path('about/', views.about, name= 'about'),
    path('contacts/', views.contacts, name='contacts'),
    path("post/<str:slug>", views.post_detal, name="post"),
    path("author/<str:at>", views.author_detal, name="author"),
    path("err", views.err, name = 'err')
]

handler404 = 'app.views.err'