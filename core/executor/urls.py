from django.urls import path
from .views import CodeExecutionView, home

urlpatterns = [
    path('', home, name='home'),
    path('execute/', CodeExecutionView.as_view(), name='execute_code'),
]