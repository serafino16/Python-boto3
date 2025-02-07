import boto3

def enable_s3_encryption(bucket_name):
    s3 = boto3.client('s3')
    s3.put_bucket_encryption(
        Bucket=bucket_name,
        ServerSideEncryptionConfiguration={
            'Rules': [
                {
                    'ApplyServerSideEncryptionByDefault': {
                        'SSEAlgorithm': 'AES256'
                    }
                }
            ]
        }
    )
    print(f'Enabled server-side encryption on bucket: {bucket_name}')


enable_s3_encryption('bucket')