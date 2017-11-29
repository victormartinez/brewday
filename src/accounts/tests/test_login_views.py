from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from model_mommy import mommy

from src.accounts.models import Profile

User = get_user_model()


class LoginViewTemplateTestCase(TestCase):
    def setUp(self):
        self.url = reverse('core:login')
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(200, self.response.status_code)

    def test_contents(self):
        contents = [
            '<h2>Login</h2>',
            '<form method="post">',
            'csrfmiddlewaretoken',
            '<input type="text" name="username"',
            '<input type="password" name="password"',
            '<input type="checkbox" name="keep_signed"',
            "<h5>Don't have an account?",
            'Forgot your password?</a>',
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)


class LoginSuccessWithEmailTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('victormartinez', 'vcrmartinez@gmail.com', '123!123!123!')
        mommy.make(Profile, user=User.objects.get(username='victormartinez'))

        self.url = reverse('core:login')
        self.response = self.client.post(
            self.url,
            data={'username': 'vcrmartinez@gmail.com', 'password': '123!123!123!'}
        )

    def test_status_code(self):
        self.assertEqual(302, self.response.status_code)

    def test_redirects(self):
        self.assertRedirects(self.response, reverse('core:app'))

    def test_user_match(self):
        user = User.objects.get(username='victormartinez')
        self.assertEquals(self.response.wsgi_request.user, user)

    def test_authenticated(self):
        self.assertTrue(self.response.wsgi_request.user.is_authenticated())

    def tearDown(self):
        User.objects.all().delete()


class LoginSuccessWithUsernameTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('victormartinez', 'vcrmartinez@gmail.com', '123!123!123!')
        mommy.make(Profile, user=User.objects.get(username='victormartinez'))

        self.url = reverse('core:login')
        self.response = self.client.post(
            self.url,
            data={'username': 'victormartinez', 'password': '123!123!123!'}
        )

    def test_status_code(self):
        self.assertEqual(302, self.response.status_code)

    def test_redirects(self):
        self.assertRedirects(self.response, reverse('core:app'))

    def test_user_match(self):
        user = User.objects.get(username='victormartinez')
        self.assertEquals(self.response.wsgi_request.user, user)

    def test_authenticated(self):
        self.assertTrue(self.response.wsgi_request.user.is_authenticated())

    def tearDown(self):
        User.objects.all().delete()


class LoginUsernameFailureTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('victormartinez', 'vcrmartinez@gmail.com', '123!123!123!')
        mommy.make(Profile, user=User.objects.get(username='victormartinez'))

        self.url = reverse('core:login')
        self.response = self.client.post(
            self.url,
            data={'username': 'admin', 'password': '123!123!123!'}
        )

    def test_status_code(self):
        self.assertEquals(200, self.response.status_code)

    def test_not_authenticated(self):
        self.assertFalse(self.response.wsgi_request.user.is_authenticated())

    def test_error_messages(self):
        message = 'Please enter a correct username and password. Note that both fields may be case-sensitive.'
        self.assertTrue(message in self.response.rendered_content)

    def tearDown(self):
        User.objects.all().delete()


class LoginEmailFailureTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('victormartinez', 'vcrmartinez@gmail.com', '123!123!123!')
        mommy.make(Profile, user=User.objects.get(username='victormartinez'))

        self.url = reverse('core:login')
        self.response = self.client.post(
            self.url,
            data={'username': 'admin@gmail.com', 'password': '123!123!123!'}
        )

    def test_status_code(self):
        self.assertEquals(200, self.response.status_code)

    def test_not_authenticated(self):
        self.assertFalse(self.response.wsgi_request.user.is_authenticated())

    def test_error_messages(self):
        message = 'Please enter a correct username and password. Note that both fields may be case-sensitive.'
        self.assertTrue(message in self.response.rendered_content)

    def tearDown(self):
        User.objects.all().delete()


class LoginPasswordFailureTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('victormartinez', 'vcrmartinez@gmail.com', '123!123!123!')
        mommy.make(Profile, user=User.objects.get(username='victormartinez'))

        self.url = reverse('core:login')
        self.response = self.client.post(
            self.url,
            data={'username': 'victormartinez', 'password': '123!123!'}
        )

    def test_status_code(self):
        self.assertEquals(200, self.response.status_code)

    def test_not_authenticated(self):
        self.assertFalse(self.response.wsgi_request.user.is_authenticated())

    def test_error_messages(self):
        message = 'Please enter a correct username and password. Note that both fields may be case-sensitive.'
        self.assertTrue(message in self.response.rendered_content)

    def tearDown(self):
        User.objects.all().delete()
