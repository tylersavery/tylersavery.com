from project.settings.constants.env import ENV

# Allowed Hosts
# https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts

ALLOWED_HOSTS = ENV.list("ALLOWED_HOSTS", default=["*"])
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
