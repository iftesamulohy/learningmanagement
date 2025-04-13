from django.urls import path
from .views import CourseDetailView, IndexView, OrderFormView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('course/<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),
    path('enroll/<slug:slug>/', OrderFormView.as_view(), name='enroll_form'),
]