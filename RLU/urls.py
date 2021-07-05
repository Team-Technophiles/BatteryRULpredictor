from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    #path('result/',views.result ,name="result")
    path('result/', views.result, name="result"),
    path('graphs/',views.graphs, name="graphs")
]
