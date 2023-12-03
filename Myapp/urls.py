from django.urls import path
from Myapp import views
from .views import index

urlpatterns = [
    #path('', views.index, name='index'),
    #path('Bluearchive/', views.BA),
    #path('Maplestroy/', views.MS),
    #path('Main/', views.main)

    #path('',views.main, name='index')
    path('', index, name='index')
]
