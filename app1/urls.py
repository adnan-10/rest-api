from django.urls import path
from app1 import views

urlpatterns =[
    path('hello-view/',views.HelloApiView.as_view()),

]
