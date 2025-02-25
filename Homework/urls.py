from django.urls import path
# from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from Homework.views import LoginView, RegistrationView, HomeworkCreate, HomeworkList, HomeworkDetail, HomeworkUpdate, HomeworkDelete  # Import your views


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # For token refresh
    path('register/', RegistrationView.as_view(), name='register'),

    path('homework/', HomeworkList.as_view(), name='homework-list'),    # GET /api/homework/ (List ALL)
    path('homework/create/', HomeworkCreate.as_view(), name='homework-create'),  # POST /api/homework/ (Create NEW)
    path('homework/<int:pk>/', HomeworkDetail.as_view(), name='homework-detail'),  # GET /api/homework/1/ (Retrieve ONE)
    path('homework/<int:pk>/update/', HomeworkUpdate.as_view(), name='homework-update'),  # PUT /api/homework/1/ (Update ONE)
    path('homework/<int:pk>/delete/', HomeworkDelete.as_view(), name='homework-delete'),  # DELETE /api/homework/1/ (Delete ONE)
]