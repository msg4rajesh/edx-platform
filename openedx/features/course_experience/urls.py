"""
Defines URLs for the course experience.
"""

from django.urls import path
from .views.course_home import outline_tab
from .views.course_updates import CourseUpdatesView

urlpatterns = [
    path('', outline_tab, name='openedx.course_experience.course_home'),
    path('updates', CourseUpdatesView.as_view(), name='openedx.course_experience.course_updates'),
]
