from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    
    # resident management
    path('mr/', views.manage_resident, name="manage-resident"),
    path('add-resident/', views.add_resident, name="add-resident"),
    path('update-resident/<str:id>/', views.update_resident, name="update-resident"),
         #address
    path('add-address/<str:id>/', views.add_address, name="add-address"),
    path('update-address/<str:id>/', views.update_address, name="update-address"),
         #house
    path('add-house/', views.add_house, name="add-house"),
    path('update-house/<str:id>/', views.update_house, name="update-house"),
         #family
    path('add-family/', views.add_family, name="add-family"),
    path('update-family/<str:id>/', views.update_family, name="update-family"),
         #id card
    path('add-idcard/', views.add_id_card, name="add-idcard"),
    path('update-idcard/<str:id>/', views.update_id_card, name="update-idcard"),
    
     # ? end of resident management
    
    
    path('mvd', views.manage_vital_data, name="manage-vital-data"),
    
    #local business management
    path('mlb', views.manage_local_business, name="manage-local-business"),
    path('add-local-business/', views.add_local_business, name="add-local-business"),
    path('update-local-business/<str:id>/', views.update_local_business, name="update-local-business"),
    path('delete-local-business/<str:id>/', views.delete_local_business, name="delete-local-business"),
        
    
    path('mkl', views.manage_kebele_land, name="manage-kebele-land"),
    path('mkl', views.manage_kebele_house, name="manage-kebele-house"),

    
]