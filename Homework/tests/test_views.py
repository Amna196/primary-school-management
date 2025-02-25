import pytest
from rest_framework import status
from Homework.models import Homework, User, Student  # Import User and Student
from django.utils import timezone
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.mark.django_db
class TestHomeworkEndpoints:
    def setup_method(self):
        self.api_client = APIClient()

        self.staff_user = User.objects.create_user(username='teststaff', password='password123', role='staff', email='staff@example.com')
        self.guardian_user = User.objects.create_user(username='testguardian', password='password123', role='guardian', email='guardian@example.com')

        # Create students and associate them with the guardian
        self.student1 = Student.objects.create(user=self.guardian_user, class_id='1A')  # Child in class 1A
        self.student2 = Student.objects.create(user=self.guardian_user, class_id='1B')  # Child in class 1B
        self.student3 = Student.objects.create(user=self.guardian_user, class_id='1C')  # Child in class 1C

        # Create homework - some for the guardian's children, some for others
        self.homework_1a = Homework.objects.create(title="1A Homework", description="Homework for 1A", due_date=timezone.now(), class_id='1A')
        self.homework_1b = Homework.objects.create(title="1B Homework", description="Homework for 1B", due_date=timezone.now(), class_id='1B')
        self.homework_2a = Homework.objects.create(title="2A Homework", description="Homework for 2A", due_date=timezone.now(), class_id='2A')  # Not for this guardian
        self.homework_3a = Homework.objects.create(title="3A Homework", description="Homework for 3A", due_date=timezone.now(), class_id='3A')  # Not for this guardian
        self.homework_1c = Homework.objects.create(title="1C Homework", description="Homework for 1C", due_date=timezone.now(), class_id='1C')  # Not for this guardian

    def test_create_homework_staff(self):
        self.api_client.force_authenticate(user=self.staff_user)
        data = {
            "title": "New Homework",
            "description": "Homework description",
            "due_date": timezone.now().isoformat(),
            "class_id": "1B"
        }
        url = reverse('homework-create')  # Use reverse
        response = self.api_client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Homework.objects.count() == 6

    def test_create_homework_guardian(self):
        self.api_client.force_authenticate(user=self.guardian_user)
        data = {
            "title": "New Homework",
            "description": "Homework description",
            "due_date": timezone.now().isoformat(),
            "class_id": "1B"  # Guardian should not be able to create for any class
        }
        url = reverse('homework-create') # Use reverse
        response = self.api_client.post(url, data, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list_homework_staff(self):
        self.api_client.force_authenticate(user=self.staff_user)
        # Homework.objects.create(title="Homework 1", due_date=timezone.now(), class_id="1B")
        url = reverse('homework-list') # Use reverse
        response = self.api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 5 

    def test_list_homework_guardian(self):
        self.api_client.force_authenticate(user=self.guardian_user)
        url = reverse('homework-list')
        response = self.api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3  # Expect 3 homework items (1A, 1B and 1C)

        # Verify the content (optional but highly recommended)
        class_ids_returned = {item['class_id'] for item in response.data}
        assert class_ids_returned == {'1A', '1B', '1C'}

    def test_detail_homework_staff(self):
        self.api_client.force_authenticate(user=self.staff_user)
        homework = Homework.objects.create(title="Homework 1", due_date=timezone.now(), class_id="1B")
        url = reverse('homework-detail', kwargs={'pk': homework.pk}) 
        response = self.api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == "Homework 1"

    def test_detail_homework_guardian(self):
        self.api_client.force_authenticate(user=self.guardian_user)
        homework = Homework.objects.create(title="Guardian's Homework", due_date=timezone.now(), class_id="1A") # Match with student's class_id
        url = reverse('homework-detail', kwargs={'pk': homework.pk})
        response = self.api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == "Guardian's Homework"

        # Test retrieving homework not related to guardian
        homework_other = Homework.objects.create(title="Other Homework", due_date=timezone.now(), class_id="2B")
        url_other = reverse('homework-detail', kwargs={'pk': homework_other.pk})
        response_other = self.api_client.get(url_other)
        assert response_other.status_code == status.HTTP_404_NOT_FOUND


    def test_update_homework_staff(self):
        self.api_client.force_authenticate(user=self.staff_user)
        homework = Homework.objects.create(title="Homework 1", description="Homework description", due_date=timezone.now(), class_id="1B")
        updated_data = {"title": "Updated Homework", "description": "Homework description", "due_date": timezone.now().isoformat(), "class_id": "1C"}
        url = reverse('homework-update', kwargs={'pk': homework.pk}) # Use reverse and pass pk
        response = self.api_client.put(url, updated_data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert Homework.objects.get(pk=homework.pk).title == "Updated Homework"

    def test_update_homework_guardian(self):
        self.api_client.force_authenticate(user=self.guardian_user)
        homework = Homework.objects.create(title="Homework 1", description="Homework description", due_date=timezone.now(), class_id="1B")
        updated_data = {"title": "Updated Homework", "description": "Homework description", "due_date": timezone.now().isoformat(), "class_id": "1C"}
        url = reverse('homework-update', kwargs={'pk': homework.pk}) # Use reverse and pass pk
        response = self.api_client.put(url, updated_data, format='json')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_delete_homework_staff(self):
        self.api_client.force_authenticate(user=self.staff_user)
        homework = Homework.objects.create(title="Homework 1", due_date=timezone.now(), class_id="1B")
        url = reverse('homework-delete', kwargs={'pk': homework.pk}) # Use reverse and pass pk
        response = self.api_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Homework.objects.count() == 5

    def test_delete_homework_guardian(self):
        self.api_client.force_authenticate(user=self.guardian_user)
        homework = Homework.objects.create(title="Homework 1", due_date=timezone.now(), class_id="1B")
        url = reverse('homework-delete', kwargs={'pk': homework.pk}) # Use reverse and pass pk
        response = self.api_client.delete(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN