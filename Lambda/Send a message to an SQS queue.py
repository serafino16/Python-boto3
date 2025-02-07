import boto3

def lambda_handler(event, context):
    sqs = boto3.client('sqs')
    response = sqs.send_message(QueueUrl='https://sqs.us-west-2.amazonaws.com/123456789012/MyQueue', MessageBody='Hello, world!')
    return {'statusCode': 200, 'body': 'Message sent to SQS successfully'}