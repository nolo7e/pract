from django.test import TestCase
from django.urls import reverse
from .models import User

class UserManagementTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_user_creation(self):
        """Проверка правильности создания пользователя"""
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.username, 'testuser')

    def test_user_login(self):
        """Проверка успешного входа пользователя"""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)  # Успешный статус после входа.
        self.assertContains(response, 'Welcome')  

    def test_admin_user_creation(self):
        """Проверка создания административного пользователя"""
        admin_user = User.objects.create_superuser(username='admin', password='adminpass')
        self.assertTrue(admin_user.is_superuser)

    def test_user_detail_view(self):
        """Проверка представления информации о пользователе"""
        response = self.client.get(reverse('user_detail', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)

    def test_user_update_view(self):
        """Проверка обновления информации о пользователе"""
        response = self.client.post(reverse('user_update', args=[self.user.id]), {
            'username': 'newusername',
            'password': 'newpassword'
        })
        self.assertEqual(response.status_code, 302)  # Проверка перенаправления после обновления
        self.user.refresh_from_db()  # Обновить экземпляр пользователя
        self.assertEqual(self.user.username, 'newusername')

    def test_user_deletion(self):
        """Проверка удаления пользователя"""
        response = self.client.post(reverse('user_delete', args=[self.user.id]))
        self.assertEqual(response.status_code, 302)  # Проверка перенаправления после удаления
        self.assertEqual(User.objects.count(), 0)
