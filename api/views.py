from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from api.models import Profile
from api.serializers import ProfileSerializer
from rest_framework.response import Response


# Create your views here
class ProfileView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            serializer = ProfileSerializer(data=request.data)
            if serializer.is_valid():
                print('Data is inserted')
                serializer.save()
                return Response({'msg':'Resume uploaded successfully','status':'success', 'candidate':serializer.data},status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors)
        except Exception as e:
            print(e)

    def get(self, request,id=None, *args, **kwargs):
        try:
            if id is not None:
                candidate = Profile.objects.get(id=id)
                serializer = ProfileSerializer(candidate)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                candidate = Profile.objects.all()
                serializer = ProfileSerializer(candidate, many=True)
                print('OK')
                return Response({'status':'success', 'candidates':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)



