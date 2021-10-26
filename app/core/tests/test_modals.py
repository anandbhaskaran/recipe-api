from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_With_email_sucessful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@anand.web.app'
        password = '12345678'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for the new user is normalized"""
        email = 'test@ANAND.WEB.APP'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_super_user(
            'test@anand.web.app',
            '12345678'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
