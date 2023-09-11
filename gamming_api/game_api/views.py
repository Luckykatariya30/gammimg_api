from rest_framework.response import Response
from .models import *
from .serializer import *
#from ilpapi import serializers
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
import sys
from django.views.decorators.csrf import csrf_protect

# boto3 using s3 bucket
import boto3



class GamesAPIView(APIView):

    def get_object(self, pk):
        try:
            return Games.objects.get(pk=pk)
        except Games.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        games = self.get_object(pk)
        serializer = GamesSerializer(games)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        games = self.get_object(pk)
        serializer = GamesSerializer(games, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":True})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        games = self.get_object(pk)
        games.delete()
        return Response({"success":True},status=status.HTTP_204_NO_CONTENT)
       

class CreategameAPIView(APIView):
    def post(self, request, format=None):
        serializer = GamesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        


class GameslistAPIView(APIView):
    """
    List all game, or create a new game.
    """
    def get(self, request, format=None):
        games = Games.objects.all()
        serializer = GamesSerializer(games, many=True)
        # file = open("api_data.json","r")
        # x = file.read()
        # finaldata = json.loads(x)
        return Response(serializer.data)

# create api profile

class CreatestudentAPIView(APIView):
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LevelByUserId(APIView):    
    def get(self, request,id, format=None):
        try:
            students=Student.objects.get(id=id)
            level= Level.objects.filter(student=students)
            serializer_context = {'request': request,}
            serializer = LevelSerializer(level, context=serializer_context, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            response={"exception_type":exc_type.__name__,
                      "filename":
                      exc_tb.tb_frame.f_code.co_filename,
                      "error_line_no":exc_tb.tb_lineno,
                      "message":"No such user"}
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)


