from project.settings.constants.env import ENV

# Cross-Origin Resource Sharing
# https://pypi.org/project/django-cors-headers/

CORS_ALLOW_METHODS = ENV.list(
    "CORS_ALLOW_METHODS", default=["DELETE", "GET", "OPTIONS", "PATCH", "POST", "PUT"]
)
CORS_ALLOW_HEADERS = ENV.list(
    "CORS_ALLOW_HEADERS",
    default=[
        "accept",
        "accept-encoding",
        "authorization",
        "content-type",
        "dnt",
        "origin",
        "user-agent",
        "x-csrftoken",
        "x-requested-with",
    ],
)
CORS_ORIGIN_ALLOW_ALL = ENV.bool("CORS_ORIGIN_ALLOW_ALL", default=False)
CORS_ORIGIN_REGEX_WHITELIST = ENV.list("CORS_ORIGIN_REGEX_WHITELIST", default=[])
CORS_ORIGIN_WHITELIST = ENV.list("CORS_ORIGIN_WHITELIST", default=[])
CORS_URLS_REGEX = ENV.str("CORS_URLS_REGEX", default="")
