from django.test import TestCase
from django.urls import reverse

from rest_framework import status

from test_app.models import User


class BaseTest(TestCase):


    def setUp(self):
        User.objects.create(email='test1@mailinator.com', username='test1', name='test1 name')
        User.objects.create(email='test2@mailinator.com', username='test2', name='test2 name')
        User.objects.create(email='test3@mailinator.com', username='test3', name='test3 name')


class FaceTestGet(BaseTest):


    def setUp(self):
        super(FaceTestGet, self).setUp()

    def test_users_list(self):
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_users_get(self):
        user = User.objects.get(name='test1 name')
        response = self.client.get("/users/"+ str(user.id) +"/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id': user.id,
            'name': 'test1 name',
            'username': 'test1',
            'is_superuser': False,
            'is_staff': False,
            'is_active': True
        })


class FaceTestUpdate(BaseTest):


    def setUp(self):
        super(FaceTestUpdate, self).setUp()

    def test_users_update(self):
        user = User.objects.get(name='test3 name')
        self.assertNotIn('Nicole Williamson', User.objects.filter().values_list('name', flat=True))
        data = {   
            "name": "Nicole Williamson",
            'username': 'test3',
        }
        response = self.client.put("/users/" +str(user.id)+ "/", data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertIn('Nicole Williamson', User.objects.filter().values_list('name', flat=True))

    def test_multi_update(self):
        data = {"is_active": "active", "ids": "2"}
        response = self.client.patch(
            reverse("update_multiple_users_status"), 
            data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class FaceTestPost(BaseTest):


    def setUp(self):
        super(FaceTestPost, self).setUp()

    def test_users_post(self):
        self.assertEqual(User.objects.count(), 3)
        response = self.client.post(
            "/users/",
            {
                "name": "Linda Jhonson",
                "username": "linda",
                "is_superuser": False,
                "is_staff": False,
                "is_active": True,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 4)
        self.assertIn('Linda Jhonson', User.objects.filter().values_list('name', flat=True))


class FaceTestDel(BaseTest):


    def setUp(self):
        super(FaceTestDel, self).setUp()

    def test_users_del(self):
        user = User.objects.get(name='test3 name')
        self.assertEqual(User.objects.count(), 3)
        response = self.client.delete("/users/"+ str(user.id) +"/")
        self.assertEqual(User.objects.count(), 2)
