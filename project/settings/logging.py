import sentry_sdk

from project.settings.constants.env import ENV
from project.settings.constants.project import PROJECT_NAME
from project.settings.constants.version import APP_VERSION

# Sentry
# https://docs.sentry.io/platforms/python/django/

try:
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=ENV.str("SENTRY_DNS", default=None),
        environment=ENV.str("ENVIRONMENT", default="undefined"),
        integrations=[DjangoIntegration()],
        release=f'{PROJECT_NAME}@{APP_VERSION["MAJOR"]}.{APP_VERSION["MINOR"]}.{APP_VERSION["PATCH"]}',
    )
except sentry_sdk.utils.BadDsn:
    pass
