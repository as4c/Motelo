import os
from dotenv import load_dotenv

load_dotenv()




AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY')

AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_KEY')

AWS_FILE_EXPIRE = 200

AWS_PRELOAD_METADATA = True

AWS_QUERYSTRING_AUTH = True

AWS_DEFAULT_ACL = None

STATICFILES_STORAGE = 'hotel.aws.utils.StaticRootS3BotoStorage'

DEFAULT_FILE_STORAGE = 'hotel.aws.utils.MediaRootS3BotoStorage' 

AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

AWS_S3_SIGNATURE_VERSION = 's3v4'

AWS_S3_REGION_NAME = 'ap-south-1'

AWS_S3_FILE_OVERWRITE = False


AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

MEDIA_URL = '%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME

MEDIA_ROOT = MEDIA_URL

AWS_STATIC_LOCATION = 'static'

STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)

STATIC_ROOT = STATIC_URL

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

AWS_HEADERS = {
    'CacheControl': 'max-age=86400',
}






