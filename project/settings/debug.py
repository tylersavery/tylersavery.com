from project.settings.constants.env import ENV

# Debug
# https://docs.djangoproject.com/en/3.1/ref/settings/#debug

DEBUG = ENV.bool("DEBUG", default=False)
