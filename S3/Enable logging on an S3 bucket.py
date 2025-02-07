import boto3

def enable_s3_logging(bucket_name, target_bucket, target_prefix):
    s3 = boto3.client('s3')
    s3.put_bucket_logging(
        Bucket=bucket_name,
        BucketLoggingStatus={
            'LoggingEnabled': {
                'TargetBucket': target_bucket,
                'TargetPrefix': target_prefix
            }
        }
    )
    print(f'Enabled logging on bucket: {bucket_name}')


enable_s3_logging('bucket', 'logbucket', 'logs/')