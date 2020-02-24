from django.contrib import admin
from django.urls import path, include
from wakerfarmer import views

from restapi.urls import router

urlpatterns = [
    path('', views.index),
    path('api/login', views.api_login),
    path('api/login_owner', views.api_login_owner),
    path('api/mills', views.apimills),
    path('api/mill/<int:mid>', views.get_mill),
    path('api/update/mill/<int:mid>', views.update_mill),
     path('api/mills_by_price', views.apimills_by_price),
    path('api/closemills/<str:lat>/<str:lng>/<str:distance>/', views.api_get_close_mills),
    path('api/register', views.api_register_farmer),
    path('api/register_owner', views.api_register_ownermill),
    path('admin/', admin.site.urls),

    # --- เพิ่มเติม
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('restapi/', include(router.urls)),
    
]
