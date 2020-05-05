from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """test creating a new user with an email is successful"""
        email = "emad@gmail.com"
        password = "123Emad"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test if the new user email is normalized"""
        email = 'emad@GMAIL.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='1234567'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating user no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='1234567'
            )

    def test_create_new_super_user(self):
        """test creating new super user"""
        user = get_user_model().objects.create_super_user(
            email='emad1@gmail.com',
            password='1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
