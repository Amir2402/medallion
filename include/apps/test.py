import boto3
from botocore.client import Config

# client = boto3.client(
#         "s3",
#         endpoint_url="http://minio:9000",
#         aws_access_key_id="URCG1V25AA6J5HCNIA2B",
#         aws_secret_access_key="MmjcbAWDPTSucguaOCdqcjKdpn+gDSj20bRK5ha2"
#         )

s3 = boto3.resource(
        "s3",
        endpoint_url="http://minio:9000",
        aws_access_key_id="URCG1V25AA6J5HCNIA2B",
        aws_secret_access_key="MmjcbAWDPTSucguaOCdqcjKdpn+gDSj20bRK5ha2"
        )
bucket = s3.Bucket('my-bucket-name')

if bucket.creation_date:
   print("The bucket exists")
else:
   print("The bucket does not exist")
   s3.create_bucket(Bucket = "my-bucket-name")