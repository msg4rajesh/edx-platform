"""
Defines URLs for course search.
"""

from django.urls import path
from .views.course_search import CourseSearchFragmentView, CourseSearchView

urlpatterns = [
    path('', CourseSearchView.as_view(),
         name='openedx.course_search.course_search_results',
         ), # MIKE TO BE DROPPED - only used in course home outline? (investigate if MFE uses)
    path('home_fragment', CourseSearchFragmentView.as_view(),
         name='openedx.course_search.course_search_results_fragment_view',
         ),
]
