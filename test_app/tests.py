from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class FaceTest(TestCase):
    def test_users_list(self):
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_get(self):
        response = self.client.get("/users/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_update(self):
        response = self.client.put(
            "/users/17",
            {
                "id": 17,
                "name": "Nicole Williamson",
                "username": "nicole",
                "is_superuser": False,
                "is_staff": False,
                "is_active": True,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_post(self):
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
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_del(self):
        response = self.client.delete("/users/17")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_multi_update(self):
        response = self.client.patch(
            reverse(
                "update_multiple_users_status",
                kwargs={"is_active": "active", "ids": "17"},
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_multi_delete(self):
        response = self.client.delete(
            reverse("delete_multiple_users", kwargs={"ids": "17"})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
