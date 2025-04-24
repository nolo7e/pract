from django.urls import path, include

urlpatterns = [
    path('api/users/', include('user_management_service.urls')),
    path('api/books/', include('book_management_service.urls')),
    path('api/borrowing/', include('borrowing_management_service.urls')),
    path('api/analytics/', include('analytics_service.urls')),
]