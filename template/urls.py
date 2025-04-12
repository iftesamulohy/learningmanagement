from django.urls import path
from .views import CourseDetailView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('course/<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),
]