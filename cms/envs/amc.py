from .aws import *

APPSEMBLER_AMC_API_BASE = AUTH_TOKENS.get('APPSEMBLER_AMC_API_BASE')
APPSEMBLER_FIRST_LOGIN_API = '/logged_into_edx'

APPSEMBLER_SECRET_KEY = AUTH_TOKENS.get("APPSEMBLER_SECRET_KEY")

INSTALLED_APPS += (
    'openedx.core.djangoapps.appsembler.sites',
)

EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = AUTH_TOKENS.get("MAILGUN_ACCESS_KEY")
MAILGUN_SERVER_NAME = AUTH_TOKENS.get("MAILGUN_SERVER_NAME")

FEATURES['ENABLE_COURSEWARE_INDEX'] = True
FEATURES['ENABLE_LIBRARY_INDEX'] = True

SEARCH_ENGINE = "search.elastic.ElasticSearchEngine"
ELASTIC_FIELD_MAPPINGS = {
    "start_date": {
        "type": "date"
    }
}
