import boto3

def delete_s3_object(bucket, object_name):
    s3 = boto3.client('s3')
    s3.delete_object(Bucket=bucket, Key=object_name)
    print(f'Deleted {object_name} from {bucket}')


delete_s3_object('bucket', 'file.txt')