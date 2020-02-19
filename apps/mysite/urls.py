from django.urls import path
from .views import IndexListView
app_name = 'mysite'


urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
]