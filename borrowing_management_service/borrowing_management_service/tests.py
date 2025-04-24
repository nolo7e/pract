from django.test import TestCase
from django.urls import reverse
from .models import Borrowing

class BorrowingManagementTests(TestCase):

    def setUp(self):
        self.borrowing = Borrowing.objects.create(user_id=1, book_id=1)

    def test_borrowing_creation(self):
        """Проверка правильности создания займа"""
        self.assertEqual(Borrowing.objects.count(), 1)
        self.assertEqual(self.borrowing.user_id, 1)

    def test_borrowing_detail_view(self):
        """Проверка представления подробностей займа"""
        response = self.client.get(reverse('borrowing_detail', args=[self.borrowing.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Borrowing')

    def test_borrowing_update_view(self):
        """Проверка обновления займа"""
        response = self.client.post(reverse('borrowing_update', args=[self.borrowing.id]), {
            'return_date': '2023-01-01'
        })
        self.assertEqual(response.status_code, 302)  # Проверка перенаправления
        self.borrowing.refresh_from_db()
        self.assertEqual(self.borrowing.return_date, '2023-01-01')

    def test_borrowing_deletion(self):
        """Проверка удаления займа"""
        response = self.client.post(reverse('borrowing_delete', args=[self.borrowing.id]))
        self.assertEqual(response.status_code, 302)  # Проверка перенаправления
        self.assertEqual(Borrowing.objects.count(), 0)

    def test_borrowing_list_view(self):
        """Проверка представления списка займов"""
        Borrowing.objects.create(user_id=2, book_id=2)
        response = self.client.get(reverse('borrowing_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Borrowing')
