#!/usr/bin/env python3

"""
Print all S3 buckets
"""

import logging
import boto3
import pprint
from botocore.exceptions import ClientError

# Retrieve the list of existing buckets
s3 = boto3.client("s3")
s3_resource = boto3.resource('s3')
response = s3.list_buckets()

# print("'Response' Object is of {} Type".format(type(response)))
#
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(response)
# print("The RAW response - {}".format(response))

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    bucket_name = bucket["Name"]
    print("BucketName: "+bucket_name)

    bucket_resource = s3_resource.Bucket(bucket_name)
    bucket_policy = bucket_resource.Policy()

    try:
        print(bucket_policy.policy)
    except ClientError as e:
        print("The bucket has no policy set")
