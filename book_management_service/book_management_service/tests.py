from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookManagementTests(TestCase):

    def setUp(self):
        self.book = Book.objects.create(title='Test Book', author='Test Author')

    def test_book_creation(self):
        """Проверка правильности создания книги"""
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(self.book.title, 'Test Book')
        self.assertEqual(self.book.author, 'Test Author')

    def test_book_detail_view(self):
        """Проверка представления деталей книги"""
        response = self.client.get(reverse('book_detail', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.title)

    def test_book_update_view(self):
        """Проверка обновления книги"""
        response = self.client.post(reverse('book_update', args=[self.book.id]), {
            'title': 'Updated Title',
            'author': 'Updated Author'
        })
        self.assertEqual(response.status_code, 302)  # Проверка перенаправления
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')
        self.assertEqual(self.book.author, 'Updated Author')

    def test_book_deletion(self):
        """Проверка удаления книги"""
        response = self.client.post(reverse('book_delete', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)  # Проверка перенаправления
        self.assertEqual(Book.objects.count(), 0)

    def test_book_list_view(self):
        """Проверка представления списка книг"""
        Book.objects.create(title='Another Book', author='Another Author')
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')
        self.assertContains(response, 'Another Book')
