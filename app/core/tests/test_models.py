from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_valid_email(self):
        '''
        test for creating a new user with an valid email
        '''
        email = 'test@test.com'
        password = 'testpass1234'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertIsNotNone(user)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        # check_password returns True if password is correct,
        # False if password is not correct

    def test_new_user_email_normalized(self):
        '''
        test the email for a new user is normalized
        '''
        email = 'test@TesT.com'
        password = 'testpass1234'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_with_invalid_email(self):
        '''test for creating user with invalid email'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='pass1234'
            )

    def test_create_new_superuser(self):
        '''test for creating new user as superuser'''
        user = get_user_model().objects.create_superuser(
            email='test@test.com',
            password='pass1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
