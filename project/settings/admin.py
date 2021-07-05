from project.settings.constants.env import ENV

# Admin
# https://docs.djangoproject.com/en/3.1/ref/contrib/admin/

ADMIN_URL_PATH = ENV.str("ADMIN_URL_PATH", default="admin/")
