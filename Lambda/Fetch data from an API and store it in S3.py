import boto3
import requests

def lambda_handler(event, context):
    response = requests.get('https://api.example.com/data')
    data = response.json()
    
    s3 = boto3.client('s3')
    s3.put_object(Bucket='mybucket', Key='data.json', Body=str(data))
    return {'statusCode': 200, 'body': 'Data fetched and stored successfully'}