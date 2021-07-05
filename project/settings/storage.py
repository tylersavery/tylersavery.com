from project.settings.constants.env import ENV


# Storage
# https://django-storages.readthedocs.io/

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# Amazon Web Services (AWS)
# https://aws.amazon.com/

AWS_ACCESS_KEY_ID = ENV.str("AWS_ACCESS_KEY_ID")
AWS_S3_REGION_NAME = ENV.str("AWS_S3_REGION_NAME")
AWS_SECRET_ACCESS_KEY = ENV.str("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = ENV.str("AWS_STORAGE_BUCKET_NAME")
AWS_DEFAULT_ACL = "public-read"
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_QUERYSTRING_AUTH = False
