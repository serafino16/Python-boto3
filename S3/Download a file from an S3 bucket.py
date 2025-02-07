import boto3

def download_file_from_s3(bucket, object_name, file_name):
    s3 = boto3.client('s3')
    s3.download_file(bucket, object_name, file_name)
    print(f'Downloaded {object_name} from {bucket} to {file_name}')


download_file_from_s3('bucket', 'file.txt', 'downloaded_file.txt')