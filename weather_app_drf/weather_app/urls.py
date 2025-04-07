from django.urls import path
from .views import get_student_info

urlpatterns = [
    path('student/', get_student_info, name='student_info'),
]