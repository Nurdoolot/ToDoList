from django.urls import path
from .views import UserRegistrationView

app_name = 'todolist'

urlpatterns = [
    path('accounts/register/', UserRegistrationView.as_view(), name='register')
]
