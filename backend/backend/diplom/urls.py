from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .controllers.course_controller import CourseListView, StartedCoursesView, CourseCreateView, CourseRetrieveView, CourseUpdateView
from .controllers.lab_controller import getLabFile
from .controllers.user_controller import UserGetView
from .controllers.lab_controller import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token/', obtain_auth_token, name='token'),
    path('user/', UserGetView.as_view()),
    # api для курсов
    path('courses/all', CourseListView.as_view()),
    path('courses/started', StartedCoursesView.as_view()),
    path('courses/new', CourseCreateView.as_view()),
    path('courses/<int:pk>', CourseRetrieveView.as_view()),
    path('courses/update/<int:pk>', CourseUpdateView.as_view()),
    # api для лаб
    path('course/labs', LabsByCourseIdView.as_view()),
    path('labs/completed', CompletedLabsView.as_view()),
    path('lab/file', getLabFile)
]