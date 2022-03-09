from django.urls import path, include

from .controllers.course_controller import CourseListView, CourseCreateView, CourseRetrieveView, CourseUpdateView

urlpatterns = [
    # api для курсов
    path('courses/all', CourseListView.as_view()),
    path('courses/new', CourseCreateView.as_view()),
    path('courses/<int:pk>', CourseRetrieveView.as_view()),
    path('courses/update/<int:pk>', CourseUpdateView.as_view()),
]