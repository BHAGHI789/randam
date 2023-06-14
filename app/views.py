from django.shortcuts import render,redirect

# Create your views here.
# myapp/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import UserProfile
from app.serializers import UserProfileSerializer

@api_view(["GET"])
def List_Profile(request):
    obj=UserProfile.objects.all()
    serializer=UserProfileSerializer(obj,many=True)
    return Response(serializer.data)



@api_view(['POST'])
def create_profile(request):
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PATCH'])
def update_profile(request, profile_id):
    profile = UserProfile.objects.get(id=profile_id)
    serializer = UserProfileSerializer(instance=profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return redirect("List_Profile")
    return Response(serializer.errors, status=400)

