"""
Views for the course home page.
"""

from lms.djangoapps.courseware.exceptions import Redirect
from openedx.features.course_experience.url_helpers import get_learning_mfe_home_url
from common.djangoapps.util.views import ensure_valid_course_key


@ensure_valid_course_key
def outline_tab(request, course_id):
    """Simply redirects to the MFE outline tab, as this legacy view for course home no longer exists."""
    raise Redirect(get_learning_mfe_home_url(course_key=course_id, url_fragment='home', params=request.GET))
