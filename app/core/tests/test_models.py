"""
Test for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""
    def test_create_user_with_email_successful(self):
        """test creating a user with an email is successful"""
        email = 'test@gmail.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
# to check if the email adn password match with the emails and passwords provided
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        sample_email = [
            ['test1@GMAIL.com', 'test1@gmail.com'],
            ['Test2@Gmail.com', 'test2@gmail.com'],
            ['TEST3@GMAIL.COM', 'test3@gmail.com'],
            ['test4@gmail.COM', 'test4@gmail.com'],
        ]

        for email, expected in sample_email:
            user = get_user_model().objects.create_user(email, 'sample123')
            print(f"User email: {user.email}, Expected: {expected}")  # Debugging
            self.assertEqual(user.email, expected)

    def test_create_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser('test@gmail.com','test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


