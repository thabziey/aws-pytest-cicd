import boto3

from AWSTestCases.aws_s3_test import aws_s3_check_if_buckets_exist
# Create S3 client
s3 = boto3.client('s3')

def test_aws_s3_check_if_buckets_exist():
    assert aws_s3_check_if_buckets_exist(s3) == True