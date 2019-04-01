from django.urls import path
from . import views

app_name ='giphy_api'
urlpatterns = [
 path('', views.GiphyListCreate.as_view(), name='calendar')
]