from django.test import TestCase
from .analytics import calculate_borrowing_statistics 

class AnalyticsTests(TestCase):

    def setUp(self):
        self.data = [
            {'user_id': 1, 'book_id': 1, 'borrowed_on': '2023-01-01', 'returned_on': '2023-01-10'},
            {'user_id': 1, 'book_id': 2, 'borrowed_on': '2023-01-05', 'returned_on': '2023-01-15'},
            {'user_id': 2, 'book_id': 3, 'borrowed_on': '2023-01-07', 'returned_on': None},
        ]

    def test_calculate_borrowing_statistics(self):
        """Проверка статистики занять"""
        statistics = calculate_borrowing_statistics(self.data)
        self.assertEqual(statistics['total_borrows'], 3)
        self.assertEqual(statistics['unique_users'], 2)

    def test_borrowing_statistics_with_empty_data(self):
        """Проверка статистики при пустых данных"""
        statistics = calculate_borrowing_statistics([])
        self.assertEqual(statistics['total_borrows'], 0)
        self.assertEqual(statistics['unique_users'], 0)
