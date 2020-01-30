from django.contrib import admin
from django.urls import path
from wakerfarmer import views

urlpatterns = [
    path('', views.index),
    path('api/login', views.api_login),
    path('api/mills', views.apimills),
    path('api/mill/<int:mid>', views.get_mill),
    path('api/update/mill/<int:mid>', views.update_mill),
     path('api/mills_by_price', views.apimills_by_price),
    path('api/closemills/<str:lat>/<str:lng>/<str:distance>/', views.api_get_close_mills),
    path('api/register', views.api_register_farmer),
    path('admin/', admin.site.urls),
    
]
