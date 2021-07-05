from project.settings.constants.env import ENV
from project.settings.constants.version import CACHE_VERSION

# Cache
# https://docs.djangoproject.com/en/3.1/ref/settings/#caches

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": f"{ENV.str('REDIS_URL')}/0",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "CONNECTION_POOL_KWARGS": ENV.dict(
#                 "CACHE_CONNECTION_POOL_KWARGS", default={}
#             ),
#             "REDIS_CLIENT_KWARGS": ENV.dict("REDIS_CLIENT_KWARGS", default={}),
#         },
#         "KEY_PREFIX": ENV.str("CACHE_KEY_PREFIX", default=""),
#         "TIMEOUT": ENV.int("CACHE_TIMEOUT", default=300),
#         "VERSION": CACHE_VERSION,
#     }
# }
# CACHE_TIMEOUT = CACHES.get("default")["TIMEOUT"]

SESSION_COOKIE_AGE = 24 * 60 * 60 * 7
