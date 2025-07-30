from rest_framework import serializers
from drones.models import DroneCategory
from drones.models import Drone
from drones.models import Pilot
from drones.models import Competition
import drones.views
from django.contrib.auth.models import User

class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
    drones = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='drone-detail'
    )
    class Meta:
        model=DroneCategory
        fields=(
            'url',
            'pk',
            'name',
            'drones'
        )

class DroneSerializer(serializers.HyperlinkedModelSerializer):
    drone_category=serializers.SlugRelatedField(queryset=DroneCategory.objects.all(),slug_field='name')
    owner=serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=Drone
        fields=(
            'url',
            'name',
            'owner',
            'drone_category',
            'manufacturing_date',
            'has_it_completed',
            'inserted_timestamp',
          

        )
class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    drone =DroneSerializer()
    class Meta:
        model = Competition
        fields=(
            'url',
            'pk',
            'distance_in_feet',
            'distance_acheivement_date',
            'drone'
        )        

class PilotSerializer(serializers.HyperlinkedModelSerializer):
    Competitions=CompetitionSerializer(many=True,read_only=True)
    gender=serializers.ChoiceField(
        choices=Pilot.GENDER_CHOICES
    ) 
    gender_description=serializers.CharField(source='get_gender_display',read_only=True)
    class Meta:
        model =Pilot
        fields=(
            'url',
            'name',
            'gender',
            'gender_description',
            'races_count',
            'inserted_timestamp',
            'Competitions'
        )
class PilotCompetitionSerializer(serializers.ModelSerializer):
    pilot=serializers.SlugRelatedField(queryset=Pilot.objects.all(),slug_field='name')
    drone=serializers.SlugRelatedField(queryset=Drone.objects.all(),slug_field='name')
    class Meta:
        model=Competition
        fields=(
            'url',
            'pk',
            'distance_in_feet',
            'pilot',
            'drone'
        )

class UserDroneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Drone
        fields=(
             'url',
            'name'
            )
class UserSerializer(serializers.HyperlinkedModelSerializer):
    drones=UserDroneSerializer(
        many=True,
        read_only=True
    ) 
    class Meta:
        model=User
        fields=(
            'url',
            'pk',
            'username',
            'drone'
        )           