from django.db import models

class Borrowing(models.Model):
    user = models.ForeignKey('user_management_service.User', on_delete=models.CASCADE)
    book = models.ForeignKey('book_management_service.Book', on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} borrowed {self.book}"
