from django.urls import path
from . import views

app_name = 'shortener'
urlpatterns = [
    path('', views.InputsView.as_view(), name="inputs"),
    path('post/', views.post, name="post"),
    path('<str:short_code>/', views.redirect, name="redirect"),
    path('<str:short_code>/details', views.details, name="details")   
]
