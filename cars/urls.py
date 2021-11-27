from django.urls import path
from . import views

urlpatterns = [
  path('', views.cars, name= 'cars'),
  path( '<int:id>', views.car_detail, name='car_detail'), #Car Detail Page by Car id
  path('search',views.search,name='search')
]