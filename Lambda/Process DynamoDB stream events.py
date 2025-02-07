import boto3

def lambda_handler(event, context):
    for record in event['Records']:
        if record['eventName'] == 'INSERT':
            new_image = record['dynamodb'][' {new_image}')
    return {'statusCode': 200, 'body': 'Stream processed successfully'}