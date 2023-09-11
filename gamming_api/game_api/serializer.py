from rest_framework import serializers
from .models import *


        
class TasksdictiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = fields = ['id','task_number','task_code','task_name']

class TasksSerializer(serializers.ModelSerializer):
    # medias=MediaSerializer(many=True, read_only=True)
    class Meta:
        model = Tasks
        fields = '__all__'



class LevelSerializer(serializers.ModelSerializer):
    # challenges=ChallengeSerializer(many=True, read_only=True)
    class Meta:
        model = Level
        fields = '__all__'


class LeveldactiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['id','level_code', 'level_number', 'level_name','price', 'discount']


class GamesSerializer(serializers.ModelSerializer):
    # levels = LevelSerializer(many=True, read_only=True)
    class Meta:
        model = Games
        fields = "__all__"



class GamesdactiveSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Games
        fields = ['id', 'game_name', 'game_type','membership_price', 'gamephoto','discount']
#         fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Student
        fields = "__all__"
