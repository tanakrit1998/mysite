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
    path('api/add_queue/<int:mid>/<int:fid>/', views.api_add_queue),
    path('api/add_price/<int:mid>/<int:fid>/<int:price>/<int:sprice>/', views.api_add_price),
    path('api/add_sprice/<int:mid>/<int:fid>/<int:sprice>/', views.api_add_sprice),
    path('api/delete_queue/<int:qid>/', views.api_delete_queue),
    path('api/update/mill/<int:mid>', views.update_mill),
    path('api/mill_detail/<int:mid>/', views.api_mill_detail),
    path('api/api_add_locations/<int:mid>/<str:lat>/<str:lng>/', views.api_add_locations),
    path('api/api_add_mill/<int:oid>/<str:name>/<str:lat>/<str:lng>/', views.api_add_mill),
    path('api/mills_by_price_mill', views.apimills_by_price_mill),
    path('api/closemills/<str:lat>/<str:lng>/<str:distance>/', views.api_get_close_mills),
    path('api/register', views.api_register_farmer),
    path('api/register_owner', views.api_register_ownermill),
    path('admin/', admin.site.urls),

    # --- เพิ่มเติม
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('restapi/', include(router.urls)),
    
]
