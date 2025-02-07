import boto3

def set_s3_lifecycle_policy(bucket_name):
    s3 = boto3.client('s3')
    lifecycle_policy = {
        'Rules': [
            {
                'ID': 'MoveToGlacier',
                'Filter': {'Prefix': ''},
                'Status': 'Enabled',
                'Transitions': [
                    {
                        'Days': 30,
                        'StorageClass': 'GLACIER'
                    }
                ]
            }
        ]
    }
    s3.put_bucket_lifecycle_configuration(Bucket=bucket_name, LifecycleConfiguration=lifecycle_policy)
    print(f'Set lifecycle policy on bucket: {bucket_name}')


set_s3_lifecycle_policy('bucket')