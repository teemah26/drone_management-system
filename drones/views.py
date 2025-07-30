from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from drones.models import DroneCategory
from drones.models import Drone
from drones.models import Pilot
from drones.models import Competition
from drones.serializer import DroneCategorySerializer 
from drones.serializer import DroneSerializer 
from drones.serializer import PilotSerializer
from drones.serializer import PilotCompetitionSerializer
import django_filters
from django_filters import AllValuesFilter,DateTimeFilter,NumberFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import AllValuesFilter,DateTimeFilter,NumberFilter
from rest_framework import filters
from rest_framework import permissions
from drones import custompermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication







class DroneCategoryList(generics.ListCreateAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-list'
    filter_fields = (
        'name',
    )
    search_fields = (
        '^name'
    )
    ordering_fields = (
        'name',
    )

class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-detail' 

class DroneList(generics.ListCreateAPIView):
    throttle_scope ='user'
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-list'
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    filterset_fields = [
        'name',
        'drone_category',
        'manufacturing_date',
        'has_it_completed',
    ]
    search_fields = [
        '^name'
    ]
    ordering_fields = [
        'name',
        'manufacturing_date',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.IsCurrentUserOrReadOnly,
    )

   
class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope ='anon'
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-detail'
class PilotList(generics.ListCreateAPIView):
    queryset = Pilot.objects.all()
    throttle_scope ='anon'
    serializer_class = PilotSerializer
    name = 'pilot-list'
    filter_backends=[DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    filter_fields = [
        'name',
        'gender',
        'races_count',
    ]
    search_fields = [
        '^name'
    ]
    ordering_fields = [
        'name',
        'races_count',]
    authentication_classes = (TokenAuthentication,
                              )
    permission_classes=(
        IsAuthenticated
    )
class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope ='anon'
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-detail'
    authentication_classes = (TokenAuthentication,
                              )
    permission_classes=(
        IsAuthenticated
    )



class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition-detail'
class CompetitionFilter(django_filters.FilterSet):
    pilot = AllValuesFilter(field_name='pilot__name')
    drone = AllValuesFilter(field_name='drone__name')
    distance_in_feet = NumberFilter(field_name='distance_in_feet', lookup_expr='exact')
    distance_from_acheivement_date = DateTimeFilter(field_name='distance_acheivement_date', lookup_expr='gte')
    distance_acheivement_date = DateTimeFilter(field_name='distance_acheivement_date', lookup_expr='lte')
    max_distance_in_feet = NumberFilter(field_name='distance_in_feet', lookup_expr='lte')
    min_distance_in_feet = NumberFilter(field_name='distance_in_feet', lookup_expr='gte')

    class Meta:
        model = Competition
        fields = ['pilot', 'drone', 'distance_in_feet', 'distance_from_acheivement_date','distance_acheivement_date', 'max_distance_in_feet', 'min_distance_in_feet'] 
class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition-list'
    filter_class = CompetitionFilter
    ordering_fields = (
        'distance_in_feet',
        'distance_acheivement_date',
    )
class ApiRoot(generics.GenericAPIView):
    name='api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'drone-categories': reverse(DroneCategoryList.name, request=request),
            'drones': reverse(DroneList.name, request=request),
            'pilots': reverse(PilotList.name, request=request),
            'competitions': reverse(CompetitionList.name, request=request),
        })


     
