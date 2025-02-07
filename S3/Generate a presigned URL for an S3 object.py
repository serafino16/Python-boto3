import boto3

def generate_presigned_url(bucket, object_name, expiration=3600):
    s3 = boto3.client('s3')
    url = s3.generate_presigned_url('get_object', Params={'Bucket': bucket, 'Key': object_name}, ExpiresIn=expiration)
    print(f'Presigned URL: {url}')


generate_presigned_url('bucket', 'file.txt')