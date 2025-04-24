from django.urls import path
from .views import user_list, user_detail

urlpatterns = [
    path('', user_list, name='user_list'),
    path('<int:id>/', user_detail, name='user_detail'),
]
