import boto3

def lambda_handler(event, context):
    sns = boto3.client('sns')
    response = sns.publish(TopicArn='arn:aws:sns:us-west-2:123456789012:MyTopic', Message='Hello, world!')
    return {'statusCode': 200, 'body': 'Notification sent to SNS successfully'}