from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_success(self):
        """Test creating a new user """
        email = 'test@gmail.com'
        password = 'azerty'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test if the email of the user is normalized """
        email = 'test@GOOGLE.COM'
        user = get_user_model().objects.create_user(email, '212ds')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test if the provided email is valid"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '3232Ze')
    
    def test_new_superuser(self):
        """test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            'support@google.com',
            'ezea'
        ) 
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)