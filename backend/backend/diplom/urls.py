from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .controllers.course_controller import CourseListView, CourseCreateView, CourseRetrieveView, CourseUpdateView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token/', obtain_auth_token, name='token'),
    # api для курсов
    path('courses/all', CourseListView.as_view()),
    path('courses/new', CourseCreateView.as_view()),
    path('courses/<int:pk>', CourseRetrieveView.as_view()),
    path('courses/update/<int:pk>', CourseUpdateView.as_view()),
]