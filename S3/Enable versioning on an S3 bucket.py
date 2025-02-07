import boto3

def enable_s3_versioning(bucket_name):
    s3 = boto3.client('s3')
    s3.put_bucket_versioning(Bucket=bucket_name, VersioningConfiguration={'Status': 'Enabled'})
    print(f'Enabled versioning on bucket: {bucket_name}')


enable_s3_versioning('bucket')