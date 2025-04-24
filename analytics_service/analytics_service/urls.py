from django.urls import path
from .views import analytics_list, analytics_detail

urlpatterns = [
    path('', analytics_list, name='analytics_list'),
    path('<int:id>/', analytics_detail, name='analytics_detail'),
]
