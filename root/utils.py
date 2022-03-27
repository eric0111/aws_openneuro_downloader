import boto3
from botocore import UNSIGNED
from botocore.config import Config

def print_files_in_folder(bucket, folder):
    s3 = boto3.resource('s3', config=Config(signature_version=UNSIGNED))
    my_bucket = s3.Bucket(bucket)

    for object_summary in my_bucket.objects.filter(Prefix=folder):
        print(object_summary.key)

