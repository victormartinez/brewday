from django.core import mail
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class RegisterViewTemplateTestCase(TestCase):
    def setUp(self):
        self.url = reverse('core:register')
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(200, self.response.status_code)

    def test_contents(self):
        contents = [
            '<h2>Create an account</h2>',
            '<form method="post"',
            'csrfmiddlewaretoken',
            '<input type="text" name="name"',
            '<input type="text" name="surname"',
            '<input type="email" name="email"',
            '<input type="text" name="username"',
            '<input type="password" name="password1"',
            '<input type="password" name="password2"',
            '<input type="checkbox" name="agree_terms"',
            "<h5>Have you already got an account?",
            'Login!</a>',
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)


class RegistrationSuccessTestCase(TestCase):
    def setUp(self):
        self.url = reverse('core:register')
        self.response = self.client.post(
            self.url,
            data={
                'name': 'Victor',
                'surname': 'Martinez',
                'username': 'vcrmartinez',
                'email': 'vcrmartinez@gmail.com',
                'password1': '123!123!123!',
                'password2': '123!123!123!',
                'agree_terms': 'on'
            }
        )

    def test_status_code(self):
        self.assertEqual(302, self.response.status_code)

    def test_redirects(self):
        self.assertRedirects(self.response, reverse('core:login'))

    def test_user_and_profile_exist(self):
        user = User.objects.get(username='vcrmartinez')
        self.assertIsNotNone(user)
        self.assertIsNotNone(user.profile)

    def test_user_info(self):
        user = User.objects.get(username='vcrmartinez')
        self.assertEquals('vcrmartinez', user.username)
        self.assertEquals('vcrmartinez@gmail.com', user.email)
        self.assertIsNotNone(user.created)

    def test_profile_info(self):
        user = User.objects.get(username='vcrmartinez')
        self.assertEquals('Victor', user.profile.name)
        self.assertEquals('Martinez', user.profile.surname)
        self.assertEquals('Victor Martinez', user.profile.full_name)
        self.assertIsNotNone(user.profile.created)

    def test_welcome_mail_is_sent(self):
        self.assertEquals(1, len(mail.outbox))

    def test_welcome_mail_info(self):
        email = mail.outbox[0]

        self.assertEquals('[BrewDay Platform] Welcome Victor', email.subject)
        self.assertEquals(['vcrmartinez@gmail.com'], email.to)
        self.assertEquals('webmaster@localhost', email.from_email)
        self.assertTrue('Hi Victor,' in email.body)
        self.assertTrue('Welcome to BrewDay platform. We highly recommend you to visit your profile and start '
                        'managing your recipes and ingredients for the next batch.' in email.body)

        self.assertTrue('Feel free also to check the various recipes available in our platform.' in email.body)
        self.assertTrue('You can login in our account by using your email (vcrmartinez@gmail.com) or username ('
                        'vcrmartinez).' in email.body)
        self.assertTrue('Best regards,' in email.body)
        self.assertTrue('BrewDay Staff' in email.body)
        self.assertIsNotNone(email.attach_alternative)
        self.assertEquals([], email.attachments)
        self.assertEquals([], email.bcc)
        self.assertEquals([], email.cc)

    def tearDown(self):
        User.objects.all().delete()


class RegisterFailureTestCase(TestCase):
    def setUp(self):
        self.url = reverse('core:register')
        self.response = self.client.post(
            self.url,
            data={
                'name': '',
                'surname': '',
                'username': '',
                'email': '',
                'password1': '',
                'password2': '',
            }
        )

    def test_status_code(self):
        self.assertEquals(200, self.response.status_code)

    def test_error_messages(self):
        errors = [
            (6, 'This field is required.'),
            (1, 'You need to accept the terms.')
        ]

        for count, expected in errors:
            with self.subTest():
                self.assertContains(self.response, expected, count)
