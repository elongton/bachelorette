from storages.backends.s3boto3 import S3Boto3Storage

StaticRootS3BotoStorage = lambda: S3Boto3Storage(location='static_bachelorette')
MediaRootS3BotoStorage  = lambda: S3Boto3Storage(location='media_bachelorette')
