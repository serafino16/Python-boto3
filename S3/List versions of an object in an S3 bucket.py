import boto3

def list_s3_object_versions(bucket, object_name):
    s3 = boto3.client('s3')
    response = s3.list_object_versions(Bucket=bucket, Prefix=object_name)
    for version in response.get('Versions', []):
        print(version['VersionId'], version['LastModified'])


list_s3_object_versions('bucket', 'file.txt')