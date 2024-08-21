from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Kurs, Urok, Subscription

class UrokTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.kurs = Kurs.objects.create(name='Test Course', description='Test Description', user=self.user)
        self.urok = Urok.objects.create(name='Test Lesson', description='Test Description', kurs=self.kurs, user=self.user)

    def test_create_urok(self):
        response = self.client.post('/urok/', {
            'name': 'New Lesson',
            'description': 'New Description',
            'kurs': self.kurs.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Urok.objects.count(), 2)

    def test_read_urok(self):
        response = self.client.get(f'/urok/{self.urok.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Lesson')

    def test_update_urok(self):
        response = self.client.put(f'/urok/{self.urok.id}/', {
            'name': 'Updated Lesson',
            'description': 'Updated Description',
            'kurs': self.kurs.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.urok.refresh_from_db()
        self.assertEqual(self.urok.name, 'Updated Lesson')

    def test_delete_urok(self):
        response = self.client.delete(f'/urok/{self.urok.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Urok.objects.count(), 0)


class SubscriptionTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.other_user = User.objects.create_user(username='otheruser', password='otherpassword')
        self.kurs = Kurs.objects.create(name='Test Course', description='Test Description', user=self.user)

    def test_subscribe(self):
        response = self.client.post('/subscription/', {'course_id': self.kurs.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Subscription.objects.filter(user=self.user, kurs=self.kurs).exists())

    def test_unsubscribe(self):
        Subscription.objects.create(user=self.user, kurs=self.kurs)
        response = self.client.post('/subscription/', {'course_id': self.kurs.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Subscription.objects.filter(user=self.user, kurs=self.kurs).exists())
