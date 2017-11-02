from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from model_mommy import mommy

from src.accounts.models import Profile

User = get_user_model()


class LoginSuccessTestCase(TestCase):
    def setUp(self):
        user = User(username='victormartinez', email='vcrmartinez@gmail.com')
        user.set_password('123!123!123!')
        user = user.save()

        mommy.make(
            Profile,
            user=user
        )

        self.url = reverse('core:login')
        self.response = self.client.post(
            self.url,
            data={'username': 'vcrmartinez@gmail.com', 'password': '123!123!123!'}
        )

    def test_status_code(self):
        self.assertEqual(302, self.response.status_code)

    def test_redirects(self):
        self.assertRedirects(self.response, reverse('accounts:profile'))

    def test_user_match(self):
        user = User.objects.get(username='victormartinez')
        self.assertEquals(self.response.wsgi_request.user, user)

    def test_authenticated(self):
        self.assertTrue(self.response.wsgi_request.user.is_authenticated())

    def tearDown(self):
        User.objects.all().delete()
