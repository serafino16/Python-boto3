import boto3

def lambda_handler(event, context):
    print('Scheduled Lambda function executed')
    return {'statusCode': 200, 'body': 'Scheduled Lambda function executed successfully'}