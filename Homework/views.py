from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema


# Create your views here.

from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from Homework.models import Homework, User, Student
from Homework.serializers import HomeworkSerializer, UserSerializer
from Homework.permissions import IsStaffOnly, IsStaffOrGuardianReadOnly, HomeworkAccessPermission


class LoginView(TokenObtainPairView):
    pass

class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

# Create (POST /api/homework/create/)
class HomeworkCreate(generics.CreateAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = [IsStaffOnly]  

class HomeworkList(generics.ListAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = [IsStaffOrGuardianReadOnly, HomeworkAccessPermission] 

    def get_queryset(self):
        user = self.request.user
        if user.role == 'guardian':
            student_classes = user.students.values_list('class_id', flat=True)  # Access related students directly
            return Homework.objects.filter(class_id__in=student_classes) # Filter by class_id
        return super().get_queryset()  # Staff sees all

# Retrieve (GET /api/homework/{id}/)
class HomeworkDetail(generics.RetrieveAPIView):
    serializer_class = HomeworkSerializer
    permission_classes = [IsStaffOrGuardianReadOnly, HomeworkAccessPermission]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'guardian':
            student_classes = user.students.values_list('class_id', flat=True)  # Get guardian's student class_ids
            return Homework.objects.filter(class_id__in=student_classes)  # Filter by class_id
        return Homework.objects.all()  # Staff sees all

# Update (PUT /api/homework/{id}/update/)
class HomeworkUpdate(generics.UpdateAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = [IsStaffOnly] 

# Delete (DELETE /api/homework/{id}/delete/)
class HomeworkDelete(generics.DestroyAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = [IsStaffOnly] 
