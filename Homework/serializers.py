from rest_framework import serializers
from Homework.models import Homework, User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, permissions
# from Homework.serializers import UserSerializer  # Create a serializer for User

class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'role')  # Include role
        extra_kwargs = {'password': {'write_only': True}}  # Make password write-only

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) # Create user with hashed password
        return user