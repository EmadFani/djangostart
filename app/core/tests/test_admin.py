from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_super_user(
            email='admin@gmail.com',
            password='1234Emad'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@gmail.com',
            password='1234Emad',
            name='test user full name'
        )

    def test_user_listed(self):
        """test users page listed"""
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """check if user edit page renders correctly"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
