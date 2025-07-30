from django.urls import path, include
from drones import views
from drones.V2 import views as v2_views

urlpatterns=[
    path('vehicle-categories/',views.DroneCategoryList.as_view(),name=views.DroneCategoryList.name),
    path('vehicle-categories/<int:pk>',views.DroneCategoryDetail.as_view(),name=views.DroneCategoryDetail.name),
    path('vehicle/',views.DroneList.as_view(),name=views.DroneList.name),
    path('vehicle/<int:pk>',views.DroneDetail.as_view(),name=views.DroneDetail.name),
    path('pilots/',views.PilotList.as_view(),name=views.PilotList.name),
    path('pilots/<int:pk>',views.PilotDetail.as_view(),name=views.PilotDetail.name),
    path('competitions/',views.CompetitionList.as_view(),name=views.CompetitionList.name),
    path('competitions/<int:pk>',views.CompetitionDetail.as_view(),name=views.CompetitionDetail.name),
    path('',v2_views.ApiRootVersion2.as_view(),name=v2_views.ApiRootVersion2.name),
]