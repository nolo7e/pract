from django.urls import path
from .views import borrowing_list, borrowing_detail

urlpatterns = [
    path('', borrowing_list, name='borrowing_list'),
    path('<int:id>/', borrowing_detail, name='borrowing_detail'),
]
